#4.Write a recursive program which accept number from user and return
#summation of its digits.
#Input : 879
#Output : 24 

iSum=0
def SummationR(iNo):
	global iSum

	if iNo > 0:
		iSum = iSum + (iNo%10)
		iNo = iNo // 10
		SummationR(iNo)
	
	return iSum

def main():

	iValue = int(input("Enter number : "))
	iRet = SummationR(iValue)
	print("Output:",iRet,end=" ")

if __name__ == '__main__':
	main()