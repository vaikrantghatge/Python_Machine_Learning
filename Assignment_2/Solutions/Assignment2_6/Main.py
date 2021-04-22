# Write a program which accept one number and display below pattern.
#  Input :  5     
#  Output :  * * * * *
#            * * * *
#            * * *
#            * *
#            * 

def Pattern(iNo):
    iCnt = 0

    for i in range(iNo + 1, 0 , -1):
        for j in range(0,i - 1):
            print("*",end=" ")
        print(" ")


def main():
    iValue = int(input("Enter first number : "))

    Pattern(iValue)

if __name__ == "__main__":
    main()