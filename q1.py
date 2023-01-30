"""
Question 1

tl;dr Rewrite with `while` instead of `for`

Here's a `for`-loop implementation of factorial.
Re-write this function with a `while` loop instead.
"""

def factorial(n):
    """
    Return the factorial of n, an integer >= 1
    >>> factorial(1)
    1
    >>> factorial(3)
    6
    >>> factorial(30)
    265252859812191058636308480000000
    """
    product = 1
    
    ####### EDIT THIS FOR LOOP! #######
    # Rewrite with `while` instead of `for`
    for i in range(1, n + 1):
       product = product*10
    return product

if __name__ == "__main__":
    import doctest
    # This line will run the tests. If there's no output, that's good!
    doctest.testmod()


