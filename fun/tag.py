#!/usr/bin/python3

import argparse
import pyperclip

def get_text(text_from_argv):
  """
  Retrieves text either from command-line arguments or clipboard.

  Args:
      text_from_argv: Text provided as a command-line argument (optional).

  Returns:
      The text to be tagged, either from the argument or clipboard.
  """
  if text_from_argv:
    return text_from_argv
  else:
    try:
      # Attempt to retrieve text from clipboard
      return pyperclip.paste()
    except:
      # If clipboard access fails, return an empty string
      return ""

def main():
  """Parses command-line arguments, generates pseudo XML for chat, and copies to clipboard."""
  parser = argparse.ArgumentParser(description="Generate pseudo XML for chat.")

  parser.add_argument("text", nargs="?", type=str, help="The text to be included within the tag (optional).")
  parser.add_argument("--tag", type=str, default="rant", help="The tag to be used for wrapping text (default: text).")
  parser.add_argument("--escape", action="store_true", default=False, help="Escape angle brackets for chat environments.")

  args = parser.parse_args()

  text = get_text(args.text)

  try:
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