#R-1.2 Write a short Python function, is even(k), that takes an
#integer value and returns True if k is even, and False otherwise. 
#However, your function cannot use the multiplication, modulo, or division operators.

def is_even(k):
    while k>1:
        k=k-2
    return True if k == 0 else False
