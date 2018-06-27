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


def chinese_remainder_theorem(y, n):
        """ This method gets the number that satisfies the theorem
        The theorem says that for each y and n:
        x = y1 (mod n1)
        x = y2 (mod n2)
        ...
        Where x is one number that satisfies the theorem
        :param y: Array of any integer numbers
        :param n: Array of pairwise coprime integers
        :return: Number satysfying the theorem
        """
        def calc_next_iteration(base, number_of_items, iterator):
            prod = 1
            for a in range(number_of_items): 
                prod *= n[a]
            return base + prod * iterator

        if len(y) != len(n) or len(y) == 0 or len(n) == 0:
            print("Incorrect number of parameters")
            return None
        val = y[0]
        for i in range(len(y) - 1):
            for j in itertools.count():
                x = calc_next_iteration(val, i + 1, j)
                if x % n[i+1] == y[i+1]:
                    val = x
                    break
        return val
