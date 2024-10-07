#!/usr/bin/python3
import sys
import PyPDF2

def  extract_first_n_pages(input_pdf, w, num_pages, num_copies ):
      """
      Extracts the first N pages from a PDF and saves them to a new PDF.

      Args:
          input_pdf (str): Path to the input PDF file.
          num_pages (int): Number of pages to extract.
      """
      with open(input_pdf, 'rb') as input_file:
        reader = PyPDF2.PdfReader(input_file)
        #TODO iterate on num_pages
        page = reader.pages[0]
        #print(page.extract_text()) #TODO a diff program
        for n in range(num_copies) :
           w.add_page(page)


filenames = sys.argv[1:]
writer = PyPDF2.PdfWriter()
num = 1  #TODO param

for f in filenames :
    print (f)
    extract_first_n_pages( f, writer, 1, num_copies=num  )
            
writer.write("output.pdf")
