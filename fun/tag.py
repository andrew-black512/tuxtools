
import argparse

def main():
  """Parses command-line arguments and generates pseudo XML for chat."""
  parser = argparse.ArgumentParser(description="Generate pseudo XML for chat.")

  # Add argument for the text to be tagged (required)
  parser.add_argument("text", type=str, help="The text to be included within the tag.")

  # Add optional argument for tag name (defaults to 'text')
  parser.add_argument("--tag", type=str, default="text",
                      help="The tag to be used for wrapping text (default: text).")

  # Add optional argument for escaping angle brackets
  parser.add_argument("--escape", action="store_true", default=False,
                      help="Escape angle brackets for chat environments.")

  # Parse arguments from the command line
  args = parser.parse_args()

  # Generate the pseudo XML output, optionally escaping angle brackets
  if args.escape:
      pseudo_xml = f"&lt;{args.tag}&gt;{args.text}&lt;/{args.tag}&gt;"
  else:
      pseudo_xml = f"<{args.tag}>{args.text}</{args.tag}>"

  # Print the result
  print(pseudo_xml)

if __name__ == "__main__":
  main()