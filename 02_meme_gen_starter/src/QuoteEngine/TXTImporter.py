from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class TXTImporter(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')
        quotes: List[QuoteModel] = []
        file = open(path,'r')
        lines = file.readline()

        for line in lines:
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split('-')
                new_quote = QuoteModel(parse[0], (parse[1]))
                quotes.append(new_quote)

        file.close()
        return quotes