import doctest

def average(iterable):
    """Computes the arithmetic mean of a list of numbers.

    >>> print average([20, 30, 70])
    40.0
    >>> print average([1, 2, 3])
    2.0
    """
    return sum(iterable, 0.0) / len(iterable)
