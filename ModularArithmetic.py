from Helper import *

class ModularArithmetic:
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
        if self.isOperationValid(other):
            value = (self.value + other.value) % self.modulus
            return ModularArithmetic(value, self.modulus)

    def __mul__(self, other):
        if self.isOperationValid(other):
            value = self.value * other.value
            return ModularArithmetic(value, self.modulus)

    def __invert__(self):
        g, a, _ = egcd(self.value, self.modulus)
        if g == 1:
            return ModularArithmetic(a, self.modulus)
        else:
            print "Modular inverse does not exist!", self.value, "mod", self.modulus
            return None

    def __str__(self):
        return str(self.value) + '%' + str(self.modulus)

    def __unicode__(self):
        return str(self.value) + '%' + str(self.modulus)

    def isOperationValid(self, other):
        """Validate operation"""
        if isinstance(other, ModularArithmetic):
            if self.modulus == other.modulus:
                return True
            else:
                raise ValueError("Modules are different")
        else:
            raise TypeError("Second element is not a valid ModularArithmetic object")

