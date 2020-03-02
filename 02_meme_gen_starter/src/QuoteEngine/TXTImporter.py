"""Make a strategy object."""

from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class TXTImporter(IngestorInterface):
    """Make a concrete strategy object for handling txt files.

    create a variable to store allowed extension
    implement parse method.
    """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Take path of directory and parse all quotes.

        Arguments:
            path {str} -- path to a directory.
        Returns:
            quotes {[QuoteModel]} -- list of quotes.
        """
        quotes = []
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')
        file = open(path, 'r')
        lines = file.readlines()
        for line in lines:
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)
        file.close()
        return quotes
