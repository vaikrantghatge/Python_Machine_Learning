# Write a program which accept one number and display below pattern.
# Input :  5     
# Output :  * * * * * 
#          * * * * * 
#          * * * * * 
#          * * * * *  
#          * * * * * 

def Pattern(iNo):
    for i in range(0,iNo,1):
        for j in range(0,iNo,1):
            print("*",end=" ")
        print(" ")

def main():
    iValue = int(input("Enter number : "))

    Pattern(iValue)

if __name__ == "__main__":
    main()