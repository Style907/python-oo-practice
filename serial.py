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
    "registers initial number to save and as a value to count"
    def __init__(self, start):
        self.start = start
        self.first = start

    "produces first serial number and adds count for next serial number"
    def generate(self):

        count = self.start
        self.start += 1
        return count
    
    "returns to initial serial number value"
    def reset(self):
        self.start = self.first


