#4.Write a program which contains filter(), map() and reduce() in it. Python application which
#contains one list of numbers. List contains the numbers which are accepted from user. Filter
#should filter out all such numbers which are even. Map function will calculate its square.
#Reduce will return addition of all that numbers.
#Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#List after filter = [2, 4, 4, 2, 8, 10]
#List after map = [4, 16, 16, 4, 64, 100]
#Output of reduce = 204 

from functools import reduce

def acceptList():
    list = []
    no=int(input("Enter number of list: "))
    for i in range(no):
        el=int(input("Enter the elements of list:"))
        list.append(el)
    return list

def main():
    lst=acceptList()
    print("Entered list is: ",lst)
    filtered=list(filter(lambda n:not(n%2),lst))
    print("Filtered Even no list:",filtered)
    mapped=list(map(lambda no:no*no,filtered))
    print("Mapped data: ",mapped)
    reduced=reduce(lambda no1,no2:no1+no2,mapped)
    print("Addition is: ",reduced)


if __name__ == '__main__':
    main()