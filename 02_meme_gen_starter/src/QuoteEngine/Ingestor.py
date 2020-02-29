from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface

from .DocxImporter import DocxImporter
from .CSVImporter import CSVImporter
from .PDFImporter import PDFImporter
from .TXTImporter import TXTImporter


class Ingestor(IngestorInterface):
    ingestors =[DocxImporter, CSVImporter, PDFImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
