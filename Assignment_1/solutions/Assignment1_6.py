#Write a program which accept number from user and check whether that number is positive or
#negative or zero.
#Input : 11 Output : Positive Number
#Input : -8 Output : Negative Number
#Input : 0 Output : Zero 
#-------------------------------------------
def ChkPos(value):
    if value < 0:
        print("Number is Negative")
    if value > 0:
        print("Number is positive")
    if value == 0:
        print("Number is nor positive not negative")
#----------------------------------------
#def ChkPos(value):
#    if value < 0:
#        print("Number is Negative")
#    else:
#        print("Number is positive")

def main():
    print("Enter the number")
    no = int(input())
    iRet = ChkPos(no)
    
if __name__ == "__main__":
    main()
        