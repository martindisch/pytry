class Reverse:
    """Iterator class for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0: raise StopIteration
        self.index -= 1
        return self.data[self.index]

def reverse(data):
    """Iterator generator for looping over a sequence backwards."""
    for index in range(len(data) - 1, -1, -1):
        yield data[index]
