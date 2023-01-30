"""
Here's a for-loop implementation of factorial.

Re-write this function with a while loop instead.
"""

def factorial(n):
    """
    Factorial Function

    For n >= 1:

    n! = n * (n-1) * (n-2) * ... * 1

    """
    product = 1
    for i in range(1, n + 1):
       product = product*i
    return product

# This code will compare your answers to the correct ones:
print(f"{factorial(1)=}  <-- this should be {math.factorial(1)}")
print(f"{factorial(3)=}  <-- this should be {math.factorial(3)}")
print(f"{factorial(5)=}  <-- this should be {math.factorial(5)}")
print(f"{factorial(6)=}  <-- this should be {math.factorial(6)}")