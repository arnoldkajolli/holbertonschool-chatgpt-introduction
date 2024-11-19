#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number recursively.
    
    Parameters:
        n (int): A non-negative integer to calculate factorial for
        
    Returns:
        int: The factorial of n (n!)
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)