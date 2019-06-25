
from distutils.core import setup
from pkgutil import walk_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


def find_packages(path=__path__, prefix=""):
    yield prefix
    prefix = prefix + "."
    for _, name, ispkg in walk_packages(path, prefix):
        if ispkg:
            yield name

import pySpinW

setup(
     name='pySpinW',
     version='0.1',
     author="Simon Ward",
     author_email="simon.ward@esss.se",
     description="Python implementation of SpinW",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/SpinW/pySpinW",
     packages = list(find_packages(pySpinW.__path__, pySpinW.__name__)),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )