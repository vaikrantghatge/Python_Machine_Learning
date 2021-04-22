#5. Write a recursive program which accept number from user and return its
#factorial.
#Input : 5
#Output : 120 

i = 1
Fact = 1
def FactorialR(iNo):
	global i
	global Fact

	if i<=iNo:
		Fact = Fact * i 
		i+=1
		FactorialR(iNo)
	return Fact

def main():

	iValue = int(input("Enter number : "))
	iRet = FactorialR(iValue)
	print("Output:",iRet,end=" ")

if __name__ == '__main__':
	main()