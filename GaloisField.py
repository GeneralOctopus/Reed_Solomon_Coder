from Helper import *

def add(x, y):
    return self.value ^ y.value

def sub(x, y):
    return self.value ^ y.value

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


class GaloisField:
    def __init__(self, dec_value, modulus):
        self.gf_exp = [0] * 512
        self.gf_log = [0] * 256
        self.init_tables(modulus)
        
        if isinstance(dec_value, int) and isinstance(modulus, int):
            if dec_value >= 0 and modulus > 0: 
                self.value = dec_value % modulus;
                self.modulus = modulus;
            else:
                raise ValueError("Value and modulus have to be greater than zero")
        else:
            raise TypeError("Value and modulus have to be integers")

    def init_tables(self, modulus):
        x = 1
        for i in range(0, 255):
            self.gf_exp[i] = x
            self.gf_log[x] = i
            x = multiplication_with_modular_reduction(x, 2, modulus)

        for i in range(255, 512):
            self.gf_exp[i] = self.gf_exp[i - 255]

        return [self.gf_log, self.gf_exp]

    def __add__(self, other):
        self.isOperationValid(other)
        value = (self.value + other.value) % self.modulus
        return GaloisField(value, self.modulus)

    def __mul__(self, other):
        self.isOperationValid(other)
        value = self.value * other.value
        return GaloisField(value, self.modulus)

    def __invert__(self):
        g, a, _ = egcd(self.value, self.modulus)
        if g == 1:
            return a%self.modulus
        else:
            print "Modular inverse does not exist!", self.value, "mod", self.modulus
            return None

    def __str__(self):
        return str(self.value) + '%' + str(self.modulus)

    def __unicode__(self):
        return str(self.value) + '%' + str(self.modulus)

    def isOperationValid(self, other):
        """Validate operation"""
        if isinstance(other, GaloisField):
            if self.modulus == other.modulus:
                pass
            else:
                raise ValueError("Modules are different")
        else:
            raise TypeError("Second element is not a valid GaloisField object")

