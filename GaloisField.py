
class GaloisField:
    def __init__(self, dec_value, modulus):
        if isinstance(dec_value, int) and isinstance(modulus, int):
            self.value = dec_value;
            self.modulus = modulus;
        else:
            raise ValueError("Value and modulus have to be integers")


