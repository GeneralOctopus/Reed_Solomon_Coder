
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

    def __sub__(self, other):
        self.isOperationValid(other)
        value = self.value - other.value
        while value < 0:
            value = self.modulus + value
        return GaloisField(value, self.modulus)

    def __mul__(self, other):
        self.isOperationValid(other)
        value = self.value * other.value
        return GaloisField(value, self.modulus)

    def isOperationValid(self, other):
        if isinstance(other, GaloisField):
            if self.modulus == other.modulus:
                pass
            else:
                raise ValueError("Modules are different")
        else:
            raise TypeError("Second element is not a valid GaloisField object")

