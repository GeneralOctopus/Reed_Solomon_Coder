from GaloisField import *
from ModularArithmetic import *

numberOne = ModularArithmetic(0,5)
numberTwo = ModularArithmetic(4,5)

print numberOne
print numberTwo
print (numberOne + numberTwo)
print (numberOne * numberTwo)
print ~numberTwo
print ~ModularArithmetic(4, 11) #przyklad z mochnackiego a=4 n=11 
                                     #~n = 4^-1 = 4^9 mod 11 = 3


print coprime(7,17)
print coprime(7,77)

numberOne = 0b10001001
numberTwo = 0b00101010

print bin(multiplication_with_modular_reduction(numberOne, numberTwo))
print bin(multiplication_with_modular_reduction(numberOne, numberTwo, 11))
print numberOne == 0b10001001
print numberTwo == 0b00101010
