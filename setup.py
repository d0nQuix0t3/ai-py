
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='ai',  
    version='0.1',
    #scripts=['ai'] ,
    author="Ryan Moos",
    author_email="",
    description="An AI Package for Processing, Modeling, Evaluating...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )