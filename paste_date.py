#!/usr/bin/python3

import argparse
import clipboard
import datetime

def format_and_copy_datetime(clip_format, stdout_format):
  """
  Formats and copies the current date and time to the clipboard and prints it to stdout.

  Args:
    clip_format: The format string for the clipboard.
    stdout_format: The format string for stdout.
  """

  now = datetime.datetime.now()

  # Format for clipboard
  clip_str = now.strftime(clip_format)
  clipboard.copy(clip_str)

  # Format for stdout
  stdout_str = now.strftime(stdout_format)
  print(stdout_str)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Format and copy datetime")
  parser.add_argument("--clip", default="%d-%m-%Y", help="Format for clipboard")
  parser.add_argument("--stdout", default="%a %d %b %Y", help="Format for stdout")
  args = parser.parse_args()

  format_and_copy_datetime(args.clip, args.stdout)

