from Helper import *

class SimpleGaloisField:
    def __add__(x, y):
        return x ^ y

    def __sub__(x, y):
        return x ^ y

    def __mul__(x, y):
    """ Carry-less multiplication"""
        z = 0
        i = 0
        while (y >> i) > 0:
            if y & (1 << i):
                z ^= x << i
            i += 1
        return z


class GaloisField:
    def __init__(self, dec_value, modulus):
        if isinstance(dec_value, int) and isinstance(modulus, int):
            if dec_value >= 0 and modulus > 0: 
                self.value = dec_value % modulus;
                self.modulus = modulus;
            else:
                raise ValueError("Value and modulus have to be greater than zero")
        else:
            raise TypeError("Value and modulus have to be integers")

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

