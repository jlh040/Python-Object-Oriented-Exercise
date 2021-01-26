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
        """Return a string representation of the instance."""

        return f'''SerialGenerator(start = {self.start} next = {self.start + 1 if self.start == self.curr_number else 
        self.curr_number})'''

    def generate(self):
        """Return the next sequential number."""

        print(self.curr_number)
        self.curr_number += 1

    def reset(self):
        """Reset the number back to the original start number"""

        self.curr_number = self.start

