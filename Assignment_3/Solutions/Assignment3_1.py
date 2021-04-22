#1.Write a program which accept N numbers from user and store it into List. Return addition of all
#elements from that List.
#Input : Number of elements : 6
#Input Elements : 13 5 45 7 4 56
#Output : 130 


def Addition(LIST):                 #while loop
    sum = 0
    i = 0
    while i < len(LIST):
        sum = sum + LIST[i]
        i = i + 1
    return sum

#def Addition(LIST):                #for loop
#    sum = 0
#    for i in range(len(LIST)):
#        sum = sum + LIST[i]
#    return sum

def main():
    arr = []
    print("Enter the number of elements : ",end=" ")
    size = int(input())
    
    for i in range(size):
        print("Enter the element no ",i+1,":",end=" ")
        value = int(input())
        arr.append(value)
        
    print("Accepted data List is : ",arr)
    
    ret = Addition(arr)
    
    print("Addition of all elements is : ",ret,end=" ")
    
if __name__ == "__main__":
    main()
