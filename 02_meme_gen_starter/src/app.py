"""Run MemeMaker application for the web."""

from flask import Flask, render_template, abort, request
from MemeEngine import MemeEngine
from QuoteEngine import QuoteModel
from QuoteEngine import Ingestor
import random
import os
import urllib.request

app = Flask(__name__)
meme = MemeEngine('./static')
images_path = "./_data/photos/dog/"
width=500

def setup():
    """Load all resources."""
    quotes = []
    quote_files = ['_data/DogQuotes/DogQuotesTXT.txt',
                   '_data/DogQuotes/DogQuotesDOCX.docx',
                   '_data/DogQuotes/DogQuotesPDF.pdf',
                   '_data/DogQuotes/DogQuotesCSV.csv']
    ingestor = Ingestor()
    for q in quote_files:
        tmp = ingestor.parse(q)
        for t in tmp:
            quotes.append(t)
    imgs = []
    imgs += [each for each in os.listdir(images_path)]
    return quotes, imgs

quotes, imgs = setup()

@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    img = images_path + img
    path = meme.make_meme(img, quote.body, quote.author, width)
    return render_template('meme.html', path=path)

@app.route('/create', methods=['GET'])
def meme_form():
    """Take user input for the meme."""
    return render_template('meme_form.html')

@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme.

    Use requests to save the image from the image_url
    form param to a temp local file. Use the meme object to generate a meme using this
    temp file and the body and author form paramaters. Remove the temporary saved image.
    """
    url_path = request.values.get('image_url')
    local_filename, headers = urllib.request.urlretrieve(url_path)
    text = request.values.get('body')
    author = request.values.get('author')
    path = meme.make_meme(local_filename, text, author, width)
    urllib.request.urlcleanup()
    return render_template('meme.html', path=path)

if __name__ == "__main__":
    """Run the application."""
    app.run()
