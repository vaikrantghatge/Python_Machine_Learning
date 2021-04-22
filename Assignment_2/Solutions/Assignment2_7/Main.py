# Write a program which accept one number and display below pattern. 
# Input :  5     
# Output : 1 2 3 4 5
#          1 2 3 4 5
#          1 2 3 4 5
#          1 2 3 4 5   
#          1 2 3 4 5
 
def Pattern(iNo):
    
    for i in range(0,iNo,1):
        for j in range(1,iNo+1):
            print(j,end=' ')
        print(" ")


def main():
    iValue = int(input("Enter first number : "))

    Pattern(iValue)

if __name__ == "__main__":
    main()