# Motivational Puppy Meme Generator

## Udacity - Intermediate Python Nanodegree

### Quote Engine Module

The Quote Engine Module is responsible for ingesting many types of files that contain quotes. A quote contains a body and an author (e.g. "this is a quote body" - Author). This module is composed of many classes. 

QuoteEngine Module contains following classes:

- __init.py
- CSVImporter
- DocxImporter
- PDFImporter
- TXTImporter
- IngestorInterface
- Ingestor
- QuoteModel

Polymorphism is achieved through IngestorInterface and Ingestor class. ...Importer files implement parse method which parse different types of files.