#!/usr/bin/python3
import argparse
import pyperclip

def main():
    """Parses command-line arguments, generates pseudo XML for chat, and copies to clipboard."""
    parser = argparse.ArgumentParser(description="Generate pseudo XML for chat.")

    parser.add_argument("--tag", type=str, default="rant", help="The tag to be used for wrapping text (default: text).")
    parser.add_argument("--escape", action="store_true", default=False, help="Escape angle brackets for chat environments.")

    args = parser.parse_args()

    try:
        # Get the text from the clipboard
        text = pyperclip.paste()

        if args.escape:
            pseudo_xml = f"&lt;{args.tag}&gt;{text}&lt;/{args.tag}&gt;"
        else:
            pseudo_xml = f"<{args.tag}>{text}</{args.tag}>"

        print(pseudo_xml)
        pyperclip.copy(pseudo_xml)
        print("Copied to clipboard!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()