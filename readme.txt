# Image Generation App

## Overview

This is a Streamlit-based Image Generation App that allows users to create images based on uploaded background images, CSV data, and custom text rendering using Google Fonts.

## Prerequisites

Make sure you have the following dependencies installed:

- [Streamlit](https://streamlit.io/)
- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)

You can typically install them using `pip`:

```
pip install streamlit Pillow
```




## Installation:

1. Create new project in PyCharm.
2. Move the files and folders to the project.
3. Run the command in terminal to install the packages into the virtual environment:
```
pip install -r requirements.txt
```

===============

1. If you are using other fonts, you may need to change the font extension (ttf, otf). You can do this in the following lines of code:

font_title_path = READY / folder_name / 'assets' / 'fonts' / 'title_font.ttf'
font_post_path = READY / folder_name / 'assets' / 'fonts' / 'post_font.otf'

The generated images will be displayed in the app, and you can find them in the project folder under the "images" subdirectory.