#1.Write a program which contains one lambda function which accepts one parameter and return
#power of two.
#Input : 4 Output : 16
#Input : 6 Output : 36 

pw = lambda no : no**2

def main():
    no = int(input("Enter number"))
    print(pw(no))

if __name__ == '__main__':
    main()