import sys
from int_tree import IntegerTriangle

def read_triangle(r):
    """
    Reads in a triangle from stdin, producing a list of rows
    r is a reader
    returns a list
    """
    return [map(int, s.split()) for s in r]

def solve_triangle(r):
    """
    Returns the maximum path of a triangle, read in from stdin
    r is a reader
    """
    t = IntegerTriangle()
    for a in read_triangle(r):
        t.add_row(a)
    return t.maximum_path()

print solve_triangle(sys.stdin)