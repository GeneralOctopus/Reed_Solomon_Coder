import GaloisField

numberOne = GaloisField.GaloisField(0,5)
numberTwo = GaloisField.GaloisField(4,5)

print numberOne
print numberTwo
print (numberOne + numberTwo)
print (numberOne * numberTwo)
print ~numberTwo
print ~GaloisField.GaloisField(4,11) #przyklad z mochnackiego a=4 n=11 
                                     #~n = 4^-1 = 4^9 mod 11 = 3
