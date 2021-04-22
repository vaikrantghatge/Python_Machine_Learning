# Write a program which contains one function named as ChkNum() which accept one
# parameter as number. If number is even then it should display “Even number” otherwise
# display “Odd number” on console.
# Input : 11 Output : Odd Number
# Input : 8 Output : Even Number 

#logic1----------------------------------------------------------
#def ChkNum(value):
#    if ((value%2)==0):
#        print("Even Number")
#    else:
#        print("Odd Number")
    
#def main():
#    print("Enter Number : ")
#    value = int(input())
#    ChkNum(value)

#Logic2------------------------------------------------------------
def ChkNum(value):
    if ((value%2)==0):
        return 1
    else:
        return 0

def main():
    print("Enter Number : ")
    value = int(input())
    ret=ChkNum(value)

    if ret==1:
        print("Even Number")
    else:
        print("Odd Number")
    
if __name__ == '__main__':
    main()
