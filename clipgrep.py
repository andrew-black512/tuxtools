
import argparse
import pyperclip
import re

def remove_lines_from_clipboard(regex, substitution_regex, append_file):
    """Removes lines matching the given regular expression from the clipboard,
    optionally substituting matched parts with a specified string, and appending
    the filtered lines to a file.

    Args:
        regex (str): The regular expression pattern to match.
        substitution_regex (str, optional): A regular expression pattern for substitution.
        append_file (str, optional): The file path to append the filtered lines to.
    """

    clipboard_text = pyperclip.paste()
    lines = clipboard_text.splitlines()

    filtered_lines = []
    for line in lines:
        compiled_regex = re.compile(regex)

# ... rest of your code

        if not compiled_regex.match(line):

        if not regex.match(line):
            filtered_lines.append(line)
        else:
            if substitution_regex:
                line = re.sub(substitution_regex, '', line)
                if line.strip():  # Keep non-empty lines after substitution
                    filtered_lines.append(line)

    new_clipboard_text = '\n'.join(filtered_lines)
    pyperclip.copy(new_clipboard_text)

    if append_file:
        with open(append_file, 'a') as f:
            f.write(new_clipboard_text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Remove lines matching a regex from the clipboard.')
    parser.add_argument('-r', '--regex', required=True, help='The regular expression pattern to match.')
    parser.add_argument('-s', '--substitution-regex', help='The regular expression pattern for substitution.')
    parser.add_argument('-a', '--append-file', help='The file path to append the filtered lines to.')
    args = parser.parse_args()

    remove_lines_from_clipboard(args.regex, args.substitution_regex, args.append_file)
