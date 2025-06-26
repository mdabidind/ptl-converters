#!/usr/bin/env python3

import sys
import os
from pdf2docx import Converter

def convert(pdf_path, docx_path):
    try:
        cv = Converter(pdf_path)
        cv.convert(docx_path, start=0, end=None)
        cv.close()
        print(f"✅ Conversion complete: {docx_path}")
        return 0
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        return 1

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: convert.py input.pdf output.docx")
        sys.exit(2)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        print(f"❌ Input file not found: {input_file}")
        sys.exit(3)

    status = convert(input_file, output_file)
    sys.exit(status)
