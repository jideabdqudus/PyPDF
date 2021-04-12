import PyPDF2
import sys, os

"""
with open("dummy.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    print(reader.getPage(0))
"""

inputs = sys.argv[1:]


def combiner(pdf_list):
    for pdf in pdf_list:
        print(pdf)


combiner(inputs)