import sys
import argparse
from PyPDF2 import PdfReader, PdfWriter
import os

def split_pdf(pdf_path, tsv_path, output_dir=None, prefix=None, offset=0):
    """Splits a PDF file based on page ranges specified in a TSV file.

    Args:
        pdf_path (str): The path to the input PDF file.
        tsv_path (str): The path to the TSV file containing names and start pages.
        output_dir (str, optional): The directory to save the split PDF files. Defaults to the current directory.
        prefix (str, optional): An optional prefix to add to the output filenames.
        offset (int, optional): An optional offset to add to each page number read from the TSV. Defaults to 0.
    """
    try:
        with open(tsv_path, 'r') as tsv_file:
            lines = tsv_file.readlines()
    except FileNotFoundError:
        print(f"Error: TSV file not found at {tsv_path}")
        return

    if len(lines) < 2:
        print("Error: TSV file must contain a header row and at least one data row.")
        return

    page_ranges = []
    try:
        header = lines[0].strip().split(',')
        name_col = header.index('Name')
        page_col = header.index('page')

        for line in lines[1:]:
            name, page_num_str = line.strip().split(',')
            try:
                page_number = int(page_num_str.strip()) + offset
                if page_number <= 0:
                    print(f"Warning: Adjusted page number for {name} is non-positive ({page_number}). Ensure the offset is appropriate.")
                page_ranges.append({'name': name.strip(), 'start_page': page_number - 1}) # Adjust to 0-based indexing
            except ValueError:
                print(f"Error: Invalid page number '{page_num_str.strip()}' in TSV for {name}. Skipping this entry.")
                continue
    except ValueError:
        print("Error: Invalid format in TSV file. Ensure each data row has 'Name' and 'page' separated by a comma.")
        return
    except IndexError:
        print("Error: Missing 'Name' or 'page' column in the TSV header.")
        return

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            total_pages = len(pdf_reader.pages)

            for i, entry in enumerate(page_ranges):
                start_page = entry['start_page']
                end_page = total_pages - 1 # Initialize to the last page

                if i + 1 < len(page_ranges):
                    end_page = page_ranges[i + 1]['start_page'] - 1

                if start_page > end_page:
                    print(f"Warning: Invalid page range for {entry['name']} after offset. Skipping.")
                    continue

                if start_page >= total_pages:
                    print(f"Warning: Start page {start_page + 1} for {entry['name']} is beyond the total number of pages. Skipping.")
                    continue

                output_pdf = PdfWriter()
                for page_num in range(start_page, end_page + 1):
                    if 0 <= page_num < total_pages:
                        output_pdf.add_page(pdf_reader.pages[page_num])
                    else:
                        print(f"Warning: Page {page_num + 1} out of bounds. Skipping for {entry['name']}.")

                output_filename_base = entry['name']
                if prefix:
                    output_filename = f"{prefix}{i+1:02d}_{output_filename_base}.pdf"
                else:
                    output_filename = f"{output_filename_base}.pdf"

                if output_dir:
                    output_path = os.path.join(output_dir, output_filename)
                else:
                    output_path = output_filename

                with open(output_path, 'wb') as output_file:
                    output_pdf.write(output_file)
                print(f"Created {output_filename} with pages {start_page + 1}-{end_page + 1} in {'the current directory' if not output_dir else output_dir}")

    except FileNotFoundError:
        print(f"Error: PDF file not found at {pdf_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split a PDF file based on page ranges in a TSV file.")
    parser.add_argument("pdf_file", help="Path to the input PDF file.")
    parser.add_argument("tsv_file", help="Path to the TSV file containing names and start pages.")
    parser.add_argument("--out", dest="output_dir", help="Optional output directory for the split PDF files.")
    parser.add_argument("--prefix", help="Optional prefix to add to the output filenames (e.g., DOC).")
    parser.add_argument("--offset", type=int, default=0, help="Optional integer offset to add to each page number in the TSV (default: 0).")

    args = parser.parse_args()

    split_pdf(args.pdf_file, args.tsv_file, args.output_dir, args.prefix, args.offset)