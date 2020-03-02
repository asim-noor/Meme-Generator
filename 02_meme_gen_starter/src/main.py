"""Run MemeMaker through Command Line Interface."""

import os
import random
import argparse
from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeEngine import MemeEngine

meme = MemeEngine('./tmp')
width=500

def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None
    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]
        img = random.choice(imgs)
    else:
        img = path
    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))
        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)
    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author, width)
    return path


if __name__ == "__main__":
    """Pass CLI arguments to make_meme method. 
    
    Arguments:
        --path {str} -- the file location for the input image (defaults=None).
        --body {str} -- the quote for the meme (defaults=None).
        --author {str} -- the author of the quote (defaults=None).
    """
    parser = argparse.ArgumentParser(description = 'Generate a Meme')
    parser.add_argument('--path', type=str,  default=None, help="Path of the file")
    parser.add_argument('--body', type=str, default=None, help="Write a quote")
    parser.add_argument('--author', type=str, default=None, help="who wrote the quote")
    args = parser.parse_args()
    path = args.path
    body = args.body
    author = args.author
    generate_meme(args.path, args.body, args.author)
