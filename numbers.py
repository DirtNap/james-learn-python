def long_division(n, d):
    """Print the quotient and remainder of n and d
    
       Arguments:
         n: a number, the divident
         d: a number, the divisor
    
    """
    q = n // d
    m = n % d
    print(n, "divided by", d, "equals", q, "with remainder", m)


num = 12345
div = 6
long_division(num, div)
