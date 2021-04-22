#Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
#for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
#parameters as number and perform the operation. Write on python program which call all the
#functions from Arithmetic module by accepting the parameters from user. 

import Arithmetic

def main():
    
    print("Enter first number : ")
    value1 = int(input())
    
    print("Enter second number : ")
    value2 = int(input())
    
    ret1 = Arithmetic.Addition(value1,value2)
    ret2 = Arithmetic.Substraction(value1,value2)
    ret3 = Arithmetic.Multiplication(value1,value2)
    ret4 = Arithmetic.Division(value1,value2)

    print("Addition is :",ret1)
    print("Substraction is : ",ret2)
    print("Multiplication is : ",ret3)
    print("Division is : ",ret4)

# Code starter
if __name__ == "__main__":
    main()
