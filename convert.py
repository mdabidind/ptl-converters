#!/usr/bin/env python3
import sys
from pdf2docx import Converter

def convert(pdf_path, docx_path):
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    try:
        convert(sys.argv[1], sys.argv[2])
    except Exception:
        sys.exit(2)
    sys.exit(0)
