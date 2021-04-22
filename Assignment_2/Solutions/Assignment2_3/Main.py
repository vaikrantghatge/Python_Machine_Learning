# Write a program which accept one number from user and return its factorial.
# Input :  5   Output : 120 

def Fact(iNo):
    Factorial = 1

    for i in range(1,iNo + 1):
        Factorial = Factorial * i

    return Factorial

def main():
    iValue = int(input("Enter first number : "))

    iRet = Fact(iValue)

    print("Factorial of {} is {}".format(iValue,iRet))


if __name__ == "__main__":
    main()