#!/usr/bin/python3

import PyPDF2
import re
import os
import pdb

# customised version of dictionary .get with default
def getanotfield(p_obj, p_fieldname) :
    print()
    value = p_obj.get(p_fieldname, F"No {p_fieldname}")
    return value

def print_annotation(p_page) :
   if "/Annots" in p_page:
        for annot in p_page["/Annots"]:
            obj = annot.get_object()
            subtype = obj["/Subtype"]
            #pdb.set_trace()
            content = obj["/Contents"]
            c = obj.get ( "/C", 'No /C' )
            print(F"Annotation: {content}   {c} ")

def count_words_in_pdf(file_path):
  """Counts the number of words in a PDF file."""

  try:
    with open(file_path, 'rb') as pdf_file:
      print()
      pdf_reader = PyPDF2.PdfReader(pdf_file)
      text = ""
      pageno = 0
      for page in pdf_reader.pages:
        pageno = pageno + 1
        print(F'Page:{pageno}')
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
  """Lists files in the current directory and displays the number of pages and words for PDF files."""
  print()
  print(f"{'File':<40}{'Pages':>10}{'Words':>20}")

  for file in os.listdir():
    if file.endswith('.pdf'):
      try:
        num_pages = len(PyPDF2.PdfReader(open(file, 'rb')).pages)
        num_words = count_words_in_pdf(file)
        print(f"{file:<40}{num_pages:>10}{num_words:>20}")
      except PyPDF2.errors.PdfReadError as e:
        print(f"Error reading {file}: {e}")
    else:
      print(file)

if __name__ == "__main__":
  list_files_with_page_counts_and_word_counts()

  