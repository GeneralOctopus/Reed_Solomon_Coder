import os

from GaloisField import *
from ModularArithmetic import *

#numberOne = ModularArithmetic(0,5)
#numberTwo = ModularArithmetic(4,5)
#
#print numberOne
#print numberTwo
#print (numberOne + numberTwo)
#print (numberOne * numberTwo)
#print ~numberTwo
#print ~ModularArithmetic(4, 11) #przyklad z mochnackiego a=4 n=11 
#                                     #~n = 4^-1 = 4^9 mod 11 = 3
#
#
#print coprime(7,17)
#print coprime(7,77)
#
#numberOne = 0b10001001
#numberTwo = 0b00101010
#
#print bin(multiplication_with_modular_reduction(numberOne, numberTwo))
#print bin(multiplication_with_modular_reduction(numberOne, numberTwo, 11))
#print numberOne == 0b10001001
#print numberTwo == 0b00101010

def display_menu():
    os.system('clear')
    print "\n"
    print "Modular arithmetic \n"
    print "\t [+] Add numbers"
    print "\t [*] Multiply numbers"
    print "\t [~] Inverse number"
    print "\t [P] Primitives"
    print "\t [C] Chinese remainder theorm"
    print "\t [q] Quit"

def press_any_key():
    raw_input("Press any key to continue...")

def get_number():
    number = int(raw_input("Write a number "))
    modulus = int(raw_input("Write a module of the number "))
    return ModularArithmetic(number, modulus)
    
def add():
    print "Set first number"
    number1 = get_number()
    print "Set second number"
    number2 = get_number()
    result = number1 + number2
    print number1, "+", number2, '=', result
    press_any_key()

def multiply():
    print "Set first number"
    number1 = get_number()
    print "Set second number"
    number2 = get_number()
    result = number1 * number2
    print number1, "+", number2, '=', result
    press_any_key()

def quit():
    display_menu()
    press_any_key()

commands = {
        '+': add,
        '*': multiply,
        'q': quit
        }

keyboard = ''
while keyboard != 'q':
    display_menu()
    keyboard = str(raw_input("\tWhat would you like to do?\n"))
    if keyboard in commands:
        commands[keyboard]()
    else:
        print("Command not found")
        press_any_key()
