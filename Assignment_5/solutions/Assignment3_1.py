#1. Write a recursive program which display below pattern.
#Input : 5
#Output : * * * * * 

i = 0
def PatternR(iNo):
	global i 
	if i!=iNo:
		print("*",end= " ")
		i+=1
		PatternR(iNo)

def main():
	
	iValue = int(input("Enter number : "))
	print("Output:",end=" ")
	PatternR(iValue)

if __name__ == '__main__':
	main()