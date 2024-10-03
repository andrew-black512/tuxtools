class HeadingPrinter:
    """Encapsulates the functionality of printing headings."""

    def __init__(self):
        self.previous_title = None

    def print_heading(self, title, offset):
        """Prints the heading if it's different from the previous one.

        Args:
            title (str): The title to be printed.
            offset (int): The offset for indentation.
        """

        if title != self.previous_title:
            self.previous_title = title
            print(" " * offset + title)

# Usage:
heading_printer = HeadingPrinter()
heading_printer_2 = HeadingPrinter()

heading_printer.print_heading("aaa",10)
heading_printer.print_heading("aaa",10)
heading_printer_2.print_heading("xxx",20)
heading_printer.print_heading("bb",10)
