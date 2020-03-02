# Motivational Puppy Meme Generator

## Udacity - Intermediate Python Nanodegree

### Meme Engine Module

The Meme Engine Module is responsible for manipulating and drawing text onto images.

MemeEngine module contains MemeEngine class.

The class is responsible for:
1. loading an image using Pillow (PIL)
2. resizing the image so the width is at most 500px and the height is scaled proportionally
3. add a quote body and a quote author to the image
4. saving the manipulated image
5. the class implements this instance method signature which returns the path to the manipulated image `make_meme(self, img_path, text, author, width=500) -> str`
