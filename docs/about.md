# About pillow-stack stack
* Stack detailing the use of the Pillow Python plugin for working with images.

## Objective
* The purpose of this stack is to facilitate image manipulation using Python's Pillow library. The template will show the use of some of the image manipulation methods implemented in the stack.

## Prerequisites
* As a prerequisite the user needs a valid images and the python installed in the system.

## How to use
* Run the commands above to create the ambient to use the stack:
```bash
python -m venv venv
. ./venv/Scripts/activate
python -m pip install --upgrade pip
pip install pillow
```
* There are two python files inserted into the template. The pillow_utils.py file contains general image handling functions. The main.py file contains running examples of image manipulation functions. This demonstrates its use.
* Insert the image file to be processed in the img_input folder.
* The processed images must be dropped into the img_output folder
* Now just run the main.py file and check the result in the specified folders.
```bash
python main.py
```