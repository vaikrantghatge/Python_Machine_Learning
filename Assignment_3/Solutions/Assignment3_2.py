#2.Write a program which accept N numbers from user and store it into List. Return Maximum
#number from that List.
#Input : Number of elements : 7
#Input Elements : 13 5 45 7 4 56 34
#Output : 56 

#logic 1:-
def Maximum(List):
	iMax = 0
	for i in range(0,len(List)):
		if List[i] > iMax:
			iMax = List[i]
	return iMax

def main():
    arr = []
    print("Enter the number of elements : ",end=" ")
    size = int(input())
    
    for i in range(size):
        print("Enter the element no ",i+1,":",end=" ")
        value = int(input())
        arr.append(value)
        
    print("Accepted data List is : ",arr)
    
    iRet =Maximum(arr)
    
    print("Maximum number from list is : ",iRet,end=" ")
    
if __name__ == "__main__":
    main()



#Logic 2:-
#    x = int(input("Enter number of elements: "))
#    list = []
#    max=0
#    for i in range(0,x):
#        el=int(input("Enter element: "))
#        list.append(el)
#        if list[i] > max:
#            max=list[i]
#    print("Max of list is", max)

#Logic 3:-
#	 x = int(input("Enter number of elements: "))
#    list = []
#    for i in range(0,x):
#        el=int(input("Enter element: "))
#        list.append(el)
#     max=max(list)
#    print("Max of list is", max)	