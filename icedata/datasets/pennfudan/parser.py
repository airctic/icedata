__all__ = ["parser", "dataset"]

from icevision.imports import *
from icevision import *
from icevision.parsers.parser import *


def parser(data_dir) -> parsers.ParserInterface:
    return PennFundanParser(data_dir=data_dir)


class PennFundanParser(Parser):
    def __init__(self, data_dir, class_map: Optional[ClassMap] = None):
        super().__init__(class_map=class_map)
        self.data_dir = data_dir
        self.filenames = get_files(data_dir / "Annotation", extensions=".txt")

    def __iter__(self):
        yield from self.filenames

    def __len__(self):
        return len(self.filenames)

    def prepare(self, o):
        self._imageid = getattr(self, "_imageid", 0) + 1
        self.lines = L(o.read_text().split("\n"))
        self._bboxes = []

        for line in self.lines:
            if line.startswith("Image filename"):
                filename = re.findall(r'"(.*)"', line)[0]
                self._filepath = self.data_dir.parent / filename

            elif line.startswith("Image size (X x Y x C)"):
                size_str = re.search(r"\d{3,4}\sx\s\d{3,4}\sx\s3", line).group()
                self._size = [int(o) for o in size_str.split("x")]

            elif line.startswith("Objects with ground truth"):
                # number of objects is the first number that shows in the line
                self._num_objects = int(re.findall("\d+", line)[0])

            elif line.startswith("Pixel mask for object"):
                mask_filename = re.findall(r'"(.+)"', line.split(":")[-1])[0]
                self._mask_filepath = self.data_dir.parent / mask_filename

            if line.startswith("Bounding box"):
                # find bbox coordinates in line and covert to a list
                point_pairs_str = re.findall(r"(\d+,\s\d+)", line)
                points = []
                for pairs in point_pairs_str:
                    for point in pairs.split(","):
                        points.append(int(point))

                bbox = BBox.from_xyxy(*points)
                self._bboxes.append(bbox)

    def imageid(self, o) -> int:
        return self._imageid

    def filepath(self, o) -> Union[str, Path]:
        return self._filepath

    def image_width_height(self, o) -> Tuple[int, int]:
        return self._size[:2]

    def labels(self, o) -> List[Hashable]:
        return ["person"] * self._num_objects

    def iscrowds(self, o) -> List[bool]:
        return [False] * self._num_objects

    def masks(self, o) -> List[Mask]:
        return [MaskFile(self._mask_filepath)]

    def bboxes(self, o) -> List[BBox]:
        return self._bboxes

    def parse_fields(self, o, record):
        record.set_filepath(self.filepath(o))
        record.set_img_size(self.image_width_height(o))

        record.detect.set_class_map(self.class_map)
        record.detect.add_labels(self.labels(o))
        record.detect.add_bboxes(self.bboxes(o))
        record.detect.add_masks(self.masks(o))


def dataset(
    data_dir: Path,
    size: int = 384,
    presize: int = 512,
    data_splitter: Optional[DataSplitter] = None,
):
    _parser = parser(data_dir=data_dir)

    train_records, valid_records = _parser.parse(data_splitter=data_splitter)

    train_tfms = tfms.A.Adapter(
        [*tfms.A.aug_tfms(size=size, presize=presize), tfms.A.Normalize()]
    )
    valid_tfms = tfms.A.Adapter([*tfms.A.resize_and_pad(size), tfms.A.Normalize()])

    train_ds = Dataset(train_records, train_tfms)
    valid_ds = Dataset(valid_records, valid_tfms)

    return train_ds, valid_ds
