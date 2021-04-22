#Write a program which accept one number for user and check whether number is prime or not. 
#Input :  5   Output : It is Prime Number 

def Prime(iNo):
    
    if iNo > 1:
        for i in range(2,iNo):
            if iNo % i != 0:
                return True
            else:
                return False
    
def main():
    iValue = int(input("Enter number : "))
    
    bRet = Prime(iValue)

    if bRet == True:
        print("{} is a prime number".format(iValue))
    else:
        print("{} is not a prime number".format(iValue))

if __name__ == "__main__":
    main()