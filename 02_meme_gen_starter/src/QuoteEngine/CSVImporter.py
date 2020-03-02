"""Make a strategy object."""

from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
import pandas as pd


class CSVImporter(IngestorInterface):
    """Make a concrete strategy object for handling CSV files.

    create a variable to store allowed extension
    implement parse method.
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Take path of directory and parse all quotes.

        Arguments:
            path {str} -- path to a directory.
        Returns:
            quotes {[QuoteModel]} -- list of quotes.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')
        quotes = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)
        return quotes
