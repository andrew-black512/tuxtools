#!/usr/bin/env python3
import sys
import re

def main():
    """
    Reads a file specified on the command line and performs the
    replacement s/\\d+\\s+/ on each line, printing the result.
    """
    # 1. Check if the filename argument is provided
    if len(sys.argv) < 2:
        print("Usage: python rep.py <filename>")
        # Note: In a direct execution script, you might change the usage to:
        # print("Usage: ./rep.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    
    # Define the regular expression pattern:
    # \d+ : one or more digits
    # \s+ : one or more whitespace characters
    digitbit = r"\d+\s+"
    xmltag = r"<[^>]*>"
    # Replacement string (empty string for deletion)
    replacement = r""

    try:
        # 2. Open and read the file
        with open(filename, 'r') as file:
            # 3. Process each line
            for line in file:
                # Perform the substitution (s/pattern/replacement/g equivalent)
                modified_line = re.sub(digitbit, replacement, line)
                
                # process useful XML-ish tags
                modified_line = re.sub(r"<ub>", "   UB:", modified_line)
                modified_line = re.sub(r"<TI>", "# ", modified_line)
                
                modified_line = re.sub(r"% ", "", modified_line)
                # double hyphen - line but not word break
                modified_line = re.sub('--\n','' , modified_line)
                
                # single hyphen - line and word break
                modified_line = re.sub('-\n',' ' , modified_line)
                
                # zap the rest
                modified_line = re.sub(xmltag, replacement, modified_line)
                
                # Print the resulting line
                print(modified_line, end='')

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
