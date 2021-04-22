#3.Write a program which contains filter(), map() and reduce() in it. Python application which
#contains one list of numbers. List contains the numbers which are accepted from user. Filter
#should filter out all such numbers which greater than or equal to 70 and less than or equal to
#90. Map function will increase each number by 10. Reduce will return product of all that
#numbers. 
#Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#List after filter = [76, 89, 86, 90, 70]
#List after map = [86, 99, 96, 100, 80]
#Output of reduce = 6538752000 

from functools import reduce

def acceptList():
    list = []
    no=int(input("Enter number of list: "))
    for i in range(no):
        el=int(input("Enter the elements of list:"))
        list.append(el)
    return list

def filFun(n):
    return 70 <= n <= 90

def mapFun(n):
    return n+10

def redFun(n1,n2):
    return n1*n2

def main():
    lst=acceptList()
    print("Entered list is: ",lst)
    filtered=list(filter(filFun,lst))
    print("Filtered list:",filtered)
    mapped=list(map(mapFun,filtered))
    print("Mapped data: ",mapped)
    reduced=reduce(redFun,mapped)
    print("Product is: ",reduced)


if __name__ == '__main__':
    main()