# Motivational Puppy Meme Generator

## Udacity - Intermediate Python Nanodegree

This project builds a "meme generator"—a multimedia application to dynamically generate memes, including an image with an overlaid quote. You can use it in browser or through command line interface.  

![demo gif](./demo.gif)

## Instruction for Use

Install the dependencies given in the requirement text. Run app.py for web version or run main.py for CLI version. 
The utility can be which can be run from the terminal by invoking `python3 main.py`

The script must take three _optional_ CLI arguments:

- `--body` a string quote body
- `--author` a string quote author
- `--path` an image path

The script returns a path to a generated image.
If any argument is not defined, a random selection is used. 

app.py runs with the a basic flask server which consumes the modules and make it usable through a web interface. The main code for this flask service is in `app.py`, templates are in `templates/` and generated images are saved to `static` directory. 


### Quote Engine Module

The Quote Engine Module is responsible for ingesting many types of files that contain quotes. A quote contains a body and an author (e.g. "this is a quote body" - Author). This module is composed of many classes. 

QuoteEngine Module contains following classes:

- __init.py
- CSVImporter
- DocxImporter
- PDFImporter
- TXTImporter
- IngestorInterface
- Ingestor
- QuoteModel


### Meme Engine Module

The Meme Engine Module is responsible for manipulating and drawing text onto images.

MemeEngine module contains MemeEngine class.

The class is responsible for:
1. loading an image using Pillow (PIL)
2. resizing the image so the width is at most 500px and the height is scaled proportionally
3. add a quote body and a quote author to the image
4. saving the manipulated image
5. the class implements this instance method signature which returns the path to the manipulated image `make_meme(self, img_path, text, author, width=500) -> str`



