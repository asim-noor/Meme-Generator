"""Create an abstract interface."""

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Define abstract IngestroInterface.

    Members:
        ingestor {[str]} -- list of allowed extensions.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Take path of file and determine it can be parsed.

        Arguments:
            path {str} -- path to a file.
        Returns:
            quotes {bool} -- true or false.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Define abstract method which take path of directory and parse all quotes.

        Arguments:
            path {str} -- path to a directory.
        Returns:
            quotes {[QuoteModel]} -- list of quotes.
        """
        pass
