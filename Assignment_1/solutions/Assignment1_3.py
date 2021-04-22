# Write a program which contains one function named as Add() which accepts two numbers
# from user and return addition of that two numbers.
# Input : 11 5 Output : 16 

#def Add(value1,value2):
#    Ans = value1+value2
#    return Ans

#def main():
#    print("Enter First Number :")
#    num1 = int(input())

#    print("Enter Second Number :")
#    num2 = int(input())

#    ret = Add(num1,num2)
#    print("Addition is :",ret)
#-----------------------------------------------------------------    
def Add(value1,value2):

    if value1 and value2 < 0:
        print("Insufficient arrguments")

    Ans = value1+value2
    return Ans

def main():
    print("Enter First Number :")
    num1 = int(input())

    print("Enter Second Number :")
    num2 = int(input())

    ret = Add(num1,num2)
    print("Addition is :",ret)

if __name__ == '__main__':
    main()
        