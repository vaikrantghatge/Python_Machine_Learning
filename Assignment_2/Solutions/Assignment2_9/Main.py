# Write a program which accept number from user and return number of digits in that number. 
# Input : 5187934   Output : 7

def Digit(iNo):
    iCnt = 0

    while iNo != 0:
        iCnt = iCnt + 1
        iNo = iNo // 10

    return iCnt


def main():
    iValue = int(input("Enter number : "))

    iRet = Digit(iValue)

    print("Count of the number is : ",iRet)


if __name__ == "__main__":
    main()