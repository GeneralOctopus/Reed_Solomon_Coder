from Helper import *

def add(x, y):
    return x ^ y

def sub(x, y):
    return x ^ y

def bit_len(x):
    length = 0
    y = x
    while y >> length:
        length += 1
    return length

def multiplication_with_modular_reduction(x, y, prim = 0):
    result = carry_less_muliplication(x, y)
    if prim > 0:
        result = carry_less_division(result, prim)
    return result

def carry_less_muliplication(x, y):
    z = 0
    i = 0
    while (y >> i) > 0:
        if y & (1 << i):
            z ^= x << i
        i += 1
    return z

def carry_less_division(x, y):
    len1 = bit_len(x)
    len2 = bit_len(y)

    if len1 < len2:
        return x

    for i in range(len1 - len2, -1, -1):
        if x & (1 << i + len2 -1):
            x ^= y << i
    return x

#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
class GaloisField:
    def __init__(self, prime=0x11):
        self.gf_exp = [0] * 512
        self.gf_log = [0] * 256
        self.prime = prime
        self.init_tables()
        
    def init_tables(self):
        x = 1
        for i in range(0, 255):
            self.gf_exp[i] = x
            self.gf_log[x] = i
            x = multiplication_with_modular_reduction(x, 2, self.prime)

        for i in range(255, 511):
            self.gf_exp[i] = self.gf_exp[i - 255]

        return [self.gf_log, self.gf_exp]

    def add(self, x, y):
        return add(x, y)

    def sub(self, x, y):
        return sub(x, y)

    def mulWithModularReduction(self, x, y, prime):
        return multiplication_with_modular_reduction(x, y, prime)

    def multiply(self, x, y):
        if x == 0 or y == 0:
            return 0

        return self.gf_exp[self.gf_log[x] + self.gf_log[y]]

    def divide(self, x, y):
        if x == 0:
            return 0

        if y == 0:
            raise ZeroDivisionError()

        return self.gf_exp[(self.gf_log[x] + 255 - self.gf_log[y]) % 255]

    def power(self, x, power):
        return self.gf_exp[(self.gf_log[x] * power) % 255]

    def inverse(self, x):
        ''' Inverse == divide(1, x) '''
        return self.gf_exp[255 - self.gf_log[x]]

    def add_polynominal(self, p, q):
        r = [0] * max(len(p), len(q))
        for i in range(0, len(p)):
            r[i + len(r) - len(p)] = p[i]
        for i in range(0, len(q)):
            r[i + len(r) - len(q)] ^= q[i]
        return r

    def multiply_polynominal(self, p, q):
        r = [0] * (len(p) + len(q) - 1)
        for i in range(0, len(q)):
            for j in range(0, len(p)):
                r[i+j] ^= self.multiply(p[i], q[j])
            return r

    def multiply_polynominal_by_number(self, p, x):
        r = [0] * len(p)
        for i in range(0, len(p)):
            r[i] = self.multiply(p[i], x)
        return r

    def polynominal_divide(self, p, q):
        msg_out = list(p)
        for i in range(0, len(p) - (len(q) - 1)):
            coef = msg_out[i]
            if coef != 0:
                for j in range(1, len(q)):
                    if divisor[j] != 0:
                        msg_out[i+j] ^= self.multiply(q[j], coef)
        separator = -(len(q) - 1)
        return msg_out[:separator], msg_out[separator:]

    def __str__(self):
        return str(self.value) + '%' + str(self.prime)

    def __unicode__(self):
        return str(self.value) + '%' + str(self.prime)
