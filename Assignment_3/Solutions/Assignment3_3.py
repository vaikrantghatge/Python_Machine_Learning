#3.Write a program which accept N numbers from user and store it into List. Return Minimum
#number from that List.
#Input : Number of elements : 4
#Input Elements : 13 5 45 7
#Output : 5

#logic 1:-
def Minimum(List):
	iMin = List[0]
	for i in range(0,len(List)):
		if List[i] < iMin:
			iMin = List[i]
	return iMin

def main():
    arr = []
    print("Enter the number of elements : ",end=" ")
    size = int(input())
    
    for i in range(size):
        print("Enter the element no ",i+1,":",end=" ")
        value = int(input())
        arr.append(value)
        
    print("Accepted data List is : ",arr)
    
    iRet =Minimum(arr)
    
    print("Minimum number from list is : ",iRet,end=" ")
    
if __name__ == "__main__":
    main()


#Logic 2:-
#    x = int(input("Enter number of elements: "))
#    list = []
#    min=list[0]
#    for i in range(0,x):
#        el=int(input("Enter element: "))
#        list.append(el)
#        if list[i] < min:
#            min=list[i]
#    print("Min of list is", min)

#Logic 3:-
#	 x = int(input("Enter number of elements: "))
#    list = []
#    for i in range(0,x):
#        el=int(input("Enter element: "))
#        list.append(el)
#     min=min(list)
#    print("Min of list is", min)	