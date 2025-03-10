#!/usr/bin/env python3

import PyPDF2
import re
import os
import pdb
import sys
import argparse

# customised version of dictionary .get with default
def getanotfield(p_obj, p_fieldname) :
    print()
    value = p_obj.get(p_fieldname, F"No {p_fieldname}")
    return value

def diagprint (text):
   print (F"   DIAG {text}")
   return 0

def print_annotation(p_page) :
   if "/Annots" in p_page:
        for annot in p_page["/Annots"]:
            obj = annot.get_object()
            subtype = obj["/Subtype"]
            if subtype == "/Link" :
               #print ("Ignore /Link")
               bodge = 1
            else :
              #pdb.set_trace()
              content = getanotfield(obj, "/Contents" ) 
              c = obj.get ( "/C", 'No /C' )
              print(F"        Annotation: {content} ")
              diagprint(F"      {subtype}   {c} ")

def print_annotations(file_path):
  """Counts the number of words in a PDF file."""

  try:
    with open(file_path, 'rb') as pdf_file:
      print()
      pdf_reader = PyPDF2.PdfReader(pdf_file)
      text = ""
      for pageno,page in enumerate(pdf_reader.pages):
        pageno = pageno + 1
        print(F'  Page:{pageno}')
        text += page.extract_text() 
        #pdb.set_trace()

        #print( text)
        print_annotation(page)


      words = re.findall(r'\w+', text)
      return len(words)
  except PyPDF2.errors.PdfReadError as e:
    print(f"Error reading {file_path}: {e}")
    return 0

def main():
    parser = argparse.ArgumentParser(description="Annotate PDF files.")
    parser.add_argument("files", nargs="+", help="PDF file(s) to annotate.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output.")
    parser.add_argument("-g", "--regex", type=str, help="Regular expression to highlight.")
    parser.add_argument("-p", "--page_numbers", action="store_true", help="Add page number annotations.")

    args = parser.parse_args()

    for filepath in args.files:
        print_annotations(filepath)
        # annotate_pdf(filepath, args.regex, args.page_numbers, args.verbose)


if __name__ == "__main__":
    main()