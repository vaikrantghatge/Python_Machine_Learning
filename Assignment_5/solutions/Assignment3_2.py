#2. Write a recursive program which display below pattern.
#Input : 5
#Output : 1 2 3 4 5 

i = 1
def PatternR(iNo):
	global i 
	if i<=iNo:
		print(i,end= " ")
		i+=1
		PatternR(iNo)

def main():
	
	iValue = int(input("Enter number : "))
	print("Output:",end=" ")
	PatternR(iValue)

if __name__ == '__main__':
	main()