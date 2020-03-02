"""Make a strategy object."""

from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
import docx


class DocxImporter(IngestorInterface):
    """Make a concrete strategy object for handling docx files.

    create a variable to store allowed extension
    implement parse method.
    """

    allowed_extensions = ['docx']

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
        quotes: List[QuoteModel] = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = QuoteModel(parse[0], (parse[1]))
                quotes.append(new_quote)
        return quotes
