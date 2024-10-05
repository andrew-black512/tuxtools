#!/usr/bin/python3

import PyPDF2
import re
import os
import pdb
import sys

# customised version of dictionary .get with default
def getanotfield(p_obj, p_fieldname) :
    print()
    value = p_obj.get(p_fieldname, F"No {p_fieldname}")
    return value

def diagprint (text):
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

def count_words_in_pdf(file_path):
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


def list_files_with_page_counts_and_word_counts():
  """Extract annotation s and other info for a Pdf."""
  
  file = sys.argv[1] 
  num_words = count_words_in_pdf(file)
  #      print(f"{file:<40}{num_pages:>10}{num_words:>20}")

if __name__ == "__main__":
  list_files_with_page_counts_and_word_counts()

  