import GaloisField

numberOne = GaloisField.GaloisField(6,5)
numberTwo = GaloisField.GaloisField(3,5)

print numberOne.value
print numberTwo.value
print (numberOne + numberTwo).value
print (numberOne - numberTwo).value
