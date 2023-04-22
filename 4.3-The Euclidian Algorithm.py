# This is an implementation of the Euclidian algorithm to find Greatest Common Divisor (GDC) of two integers a and b
# Time Complexity - O(logb)
def gdc(a, b):
    x = a
    y = b
    while y != 0:
        r = x % y
        x = y
        y = r
    
    return(x)

