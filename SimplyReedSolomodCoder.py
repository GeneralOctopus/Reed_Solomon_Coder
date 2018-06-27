from ModularArithmetic import *

class SimpleReedSolomonCoder:
    def __init__(self, nsym, prime=0x11):
        self.GF = GaloisField(prime)
