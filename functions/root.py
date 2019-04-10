from . import binary_search

def root(a, n):
    int_part = binary_search.binary_search(a, n)

    decimal_part = binary_search.binary_search(a, n, int_part)

    total = str(int_part) + str(decimal_part)[1:]

    return float(total)
