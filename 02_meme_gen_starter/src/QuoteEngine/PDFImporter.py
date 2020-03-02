"""Make a strategy object."""

from typing import List
import subprocess
import os
import random
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class PDFImporter(IngestorInterface):
    """Make a concrete strategy object for handling PDF files.

    create a variable to store allowed extension
    implement parse method.
    """
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Take path of directory and parse all quotes.

        Arguments:
            path {str} -- path to a directory.
        Returns:
            quotes {[QuoteModel]} -- list of quotes.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        tmp = f'./tmp/{random.randint(0, 100000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])
        file_ref = open(tmp, "r")
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)
        file_ref.close()
        os.remove(tmp)
        return quotes
