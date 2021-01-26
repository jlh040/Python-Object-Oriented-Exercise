"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Set the starting number."""
        self.start = start
        self.curr_number = start
    
    def __repr__(self):
        return f'SerialGenerator(start = {self.start})'

    def generate(self):
        """Return the next sequential number."""
        print(self.curr_number)
        self.curr_number += 1

    def reset(self):
        """Reset the number back to the original start number"""
        self.curr_number = self.start

