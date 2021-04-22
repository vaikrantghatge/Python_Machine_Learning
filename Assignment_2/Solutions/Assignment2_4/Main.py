#.Write a program which accept one number form user and return addition of its factors. 
# Input :  12   Output : 16  (1+2+3+4+6) 

def Factors(iNo):
    Sum = 0

    for i in range(1 , iNo):
        if iNo % i == 0:
            Sum = Sum + i

    return Sum; 

def main():
    iValue = int(input("Enter number : "))

    iRet = Factors(iValue)
    print("{} Addition of its factor is {}".format(iValue,iRet))

if __name__ == "__main__":
    main()