import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='pySpinW',
     version='0.1',
     author="Simon Ward",
     author_email="simon.ward@esss.se",
     description="Python implementation of SpinW",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/SpinW/pySpinW",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )