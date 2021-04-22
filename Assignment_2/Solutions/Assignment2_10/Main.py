#Write a program which accept number from user and return addition of digits in that number. 
#Input : 5187934   Output : 37

def Digit(iNo):
    iSum = 0
    iCnt = 0

    while iNo > 0:
        iSum = iSum + (iNo % 10)
        iNo = iNo // 10
        iCnt = iCnt + 1

    return iSum


def main():
    iValue = int(input("Enter number : "))

    iRet = Digit(iValue)

    print("Count of the number is : ",iRet)


if __name__ == "__main__":
    main()