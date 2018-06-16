def gcd(x, y):
    """Euclidean Algorythm - calculate and return the Gratest Common Divisor of two numbers(x, y)"""
    while y != 0:
        (x, y) = (y, x%y)
    return x


def egcd(x, y):
    """Extended Euclidean Algorythm - calculate the Gratest Common Divisor of two numbers(x, y)
       and return coefficients of x and y from equation:
       ax + by = 1
    """
    a0, a1 = 1, 0
    b0, b1 = 0, 1
    while y != 0:
        q = x // y
        (x, y) = (y, x%y)
        (a0, a1) = (a1, a0 - q*a1)
        (b0, b1) = (b1, b0 - q*b1)
    return x, a0, b0


def coprime(x, y):
    """Are numbers co prime?
       condition
       if GCD(x, y) == 1 numbers are coprime
    """
    return gcd(x, y) == 1 


def euler_totient(x):
    """Euler totiem needed for counting number of generators
    """
    amount = 0
    for k in range(1, x + 1):
        b, _, __ = egcd(x, k)
        if b == 1:
            amount += 1

    return amount

