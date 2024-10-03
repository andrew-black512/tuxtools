class HeadingPrinter:
    """Encapsulates the functionality of printing headings."""

    def __init__(self, offset ):
        self.previous_title = None
        self.offset = offset

    def print_heading(self, title, offset):
        """Prints the heading if it's different from the previous one.

        Args:
            title (str): The title to be printed.
            offset (int): The offset for indentation.
        """

        if title != self.previous_title:
            self.previous_title = title
            print(" " * self.offset + title)

# Usage:
heading_printer = HeadingPrinter(10)
heading_printer_2 = HeadingPrinter(11)

heading_printer.print_heading("aaa",10)
heading_printer.print_heading("aaa",10)
heading_printer_2.print_heading("xxx",20)
heading_printer.print_heading("bb",10)
