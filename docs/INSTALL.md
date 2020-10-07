!!! danger "Important"  
    We currently only support Linux/MacOS installations

## A- Installation using pip

### **Option 1:** Installing from pypi repository **[Stable Version]**
 
To install icedata package together with all dependencies:

<div class="termy">
```console
$ pip install icedata
```
</div>


### **Option 2:** Installing an editable package locally **[For Developers]**

!!! info "Note"  
    This method is used by developers who are usually either:

    - actively contributing to `icedata` project by adding new features or fixing bugs, or 

    - creating their own extensions, and making sure that their source code stay in sync with the `icedata` latest version.

Clone the repo and install the package:
<div class="termy">
```console
$ git clone --depth=1 https://github.com/airctic/icedata.git
$ cd icedata
$ pip install -e ".[all,dev]"
```


### **Option 3:** Installing a non-editable package from GitHub **[Recommended for Active Users]**

To install the icedata package from its GitHub repo, run the command here below. This option can be used in Google Colab,
for example, where you might install the icedata latest version (from the `master` branch)

<div class="termy">
```console
$ pip install git+git://github.com/airctic/icedata.git --upgrade
```
</div>


## B- Installation using conda
Creating a conda environment is considered as a best practice because it avoids polluting the default (base) environment, and reduces dependencies conflicts. Use the following command in order to create a conda environment called **ice**

<div class="termy">
```console
$ conda create -n ice python=3.8 anaconda
$ conda activate ice
$ pip install git+git://github.com/airctic/icedata.git#egg=icedata
```
</div>


!!! info "Note" 
    You can check out the following blog post: [3 ways to pip install a package ](https://ai-fast-track.github.io/blog/python/2020/03/17/how-to-pip-install-package.html) for more a detailed explantion on how to choose the most convenient installation option for you. 

