"""Implement IngestorInterface."""

from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .DocxImporter import DocxImporter
from .CSVImporter import CSVImporter
from .PDFImporter import PDFImporter
from .TXTImporter import TXTImporter


class Ingestor(IngestorInterface):
    """Implement IngestroInterface for easy access of all type of files.

    Members:
        ingestor {[str]} -- list of allowed extensions.
    """

    ingestors = [DocxImporter, CSVImporter, PDFImporter, TXTImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Take path of directory and parse all quotes.

        Arguments:
            path {str} -- path to a directory.
        Returns:
            quotes {[QuoteModel]} -- list of quotes.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
