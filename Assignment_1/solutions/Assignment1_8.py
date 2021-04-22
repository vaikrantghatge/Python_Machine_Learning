#Write a program which accept number from user and print that number of “*” on screen.
#Input : 5 Output : * * * * * 

def PrintStar(value):
    iCnt = 0
    while iCnt!=value:
        print("*", end=" ")
        iCnt = iCnt+1

def main():
    print("Enter number")
    no =int(input())
    PrintStar(no)

if __name__ == '__main__':
    main()