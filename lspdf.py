#!/usr/bin/python3

import PyPDF2
import re
import os
import pdb

def count_words_in_pdf(file_path):
  """Counts the number of words in a PDF file."""

  try:
    with open(file_path, 'rb') as pdf_file:
      print()
      pdf_reader = PyPDF2.PdfReader(pdf_file)
      text = ""
      # accumulate text to see if it is textual of scanned
      for page in pdf_reader.pages:
        text += page.extract_text() 
        #pdb.set_trace()
        #print( text)

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

  