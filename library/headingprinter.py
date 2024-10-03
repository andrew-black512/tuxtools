class HeadingPrinter:
    """Encapsulates the functionality of printing headings."""

    def __init__(self, offset ):
        """Creates a heading object

        Args:
            offset (int): The offset for indentation.
        
        """
        self.previous_title = None
        self.offset = offset

    def print_heading(self, title):
        """Prints the heading if it's different from the previous one.

        Args:
            title (str): The title to be printed.
        """

        if title != self.previous_title:
            self.previous_title = title
            print(" " * self.offset + title)

# Usage:
heading_printer = HeadingPrinter(10)
heading_printer_2 = HeadingPrinter(11)

heading_printer.print_heading("aaa")
heading_printer.print_heading("aaa")
heading_printer_2.print_heading("xxx")
heading_printer.print_heading("bb")
