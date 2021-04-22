#3.Write a recursive program which display below pattern.
#Input : 5
#Output : 5 4 3 2 1 

i=1
def PatternR(iNo):
	global i
	if i<=iNo:
		print(iNo,end=" ")
		iNo -=1
		PatternR(iNo)

def main():

	iValue = int(input("Enter number : "))
	print("Output:",end=" ")
	PatternR(iValue)

if __name__ == '__main__':
	main()