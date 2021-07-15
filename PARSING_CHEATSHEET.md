# Parsing Cheatsheet
The goal is to create a resource that will help both beginners and advanced users to easily create their parsers by providing some frequently used code snippets and best practices

## Useful example
[Custom Parser](https://airctic.com/custom_parser/)

## Use template generator
The IceVision template generator helps you to generate all the methods that you need to implement based on the parsers mixins. 
The first step is to create a class that inherits from these smaller building blocks called mixins:

!!! warning "Mixins" 
    This is just an example, choose the mixins that are relevant to your use case.

```
class WheatParser(parsers.FasterRCNN, parsers.FilepathMixin, parsers.SizeMixin):
    pass
```
We use a method called `generate_template` that will print out all the necessary methods we have to implement.

`WheatParser.generate_template()`

**Output:**
```
def __iter__(self) -> Any:
def height(self, o) -> int:
def width(self, o) -> int:
def filepath(self, o) -> Union[str, Path]:
def bboxes(self, o) -> List[BBox]:
def labels(self, o) -> List[int]:
def record_id(self, o) -> Hashable:
```

If, for example, all the images are `.jpg` and located in the `data_dir` folder, the `image_paths` attribute will be set as follow:
```
def __init__(self, data_dir):
        self.image_paths = get_files(data_dir, extensions=[".jpg"])
```

## Files code snippets
Let's suppose we have the follwoing `fname` variable:

```
fname = Path("PennFudanPed/PNGImages/FudanPed00002.png")
```
Some useful methods are listed below:

|fname                      | PennFudanPed/PNGImages/FudanPed00002.png  |
| :------------------------ | :---------------------------------------- |
|fname.exists()             | True                                      |
|fname.with_suffix('.txt')  | PennFudanPed/PNGImages/FudanPed00002.txt  |
|fname.stem                 | FudanPed00002                             |


## Parsing code snippets

#### Read a CSV file using pandas
```
import pandas as pd
df = pd.read_csv("path/to/csv/file")
df.head() # or df.sample()
```

#### Example of parsing bboxes attributes defined as an array, and stored in a string:
```
bbox = "[834.0, 222.0, 56.0, 36.0]"`
xywh = np.fromstring(bbox[1:-1], sep=",")
print(xywh)
```
**Output:** `array([834., 222.,  56.,  36.])`

#### Example of parsing bboxes attributes defined as a string with a blank separator
```
label = "2 0.527267 0.702972 0.945466 0.467218"
xywh = np.fromstring(label, sep=" ")[1:]
print(xywh)
```
**Output:** `array([0.527267, 0.702972, 0.945466, 0.467218])`

### Masks
Let's assume we have the following dictionnary entries to parse in order to create the corresponding masks. Check out the full dictionnary [annotations.json](https://github.com/airctic/icevision/blob/master/samples/annotations.json)
```
"annotations": [
    {
      "segmentation": [
        [457.3, 258.92, 458.38, 276.22, 467.03, 289.19, 473.51, 305.41, 483.24, 334.59,...]
      ],
      "area": 43522.80595,
      "iscrowd": 0,
      "image_id": 343934,
      "bbox": [
        175.14,
        175.68,
        321.08,
        240
      ],
      "category_id": 4,
      "id": 150977
    },
    {
      "segmentation": [
        [507.9, 413.08, ...]
    ...
    }
    ...
]
```

We can implement the abstract method `masks()`, defined in the abstract class `MasksMixin` that is inhereted by the `MaskRCNN` class (see [parsers documentation](https://airctic.com/parser/)), as follow:

```
class COCOAnnotationParser(MaskRCNN, COCOBBoxParser):
    def masks(self, o) -> List[MaskArray]:
        seg = o["segmentation"]
        if o["iscrowd"]:
            return [RLE.from_coco(seg["counts"])]
        else:
            return [Polygon(seg)]
```
