#4.Write a program which accept N numbers from user and store it into List. Accept one another
#number from user and return frequency of that number from List.
#Input : Number of elements : 11
#Input Elements : 13 5 45 7 4 56 5 34 2 5 65
#Element to search : 5
#Output : 3 


def searchnum(lst):
    print("Enter number to check frequency : ",end=" ")
    y = int(input())
    count = 0
    for i in range(0, x):
        if lst[i] == y:
            count = count + 1
    print("frequency of number is : ", count,end=" ")

def acceptlist():
    list = []
    for i in range(0,x):
        el=int(input("Enter elements of list : "))
        list.append(el)
    searchnum(list)

if __name__ == '__main__':
    x = int(input("Enter number of elements : "))
    acceptlist()