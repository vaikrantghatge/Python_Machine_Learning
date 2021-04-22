#5.Write a program which contains filter(), map() and reduce() in it. Python application which
#contains one list of numbers. List contains the numbers which are accepted from user. Filter
#should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
#return Maximum number from that numbers. (You can also use normal functions instead of
#lambda functions).
#Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
#List after filter = [2, 11, 17, 23, 31]
#List after map = [4, 22, 34, 46, 62]
#Output of reduce = 62 

from functools import reduce

def acceptList():
    list = []
    no=int(input("Enter number of list: "))
    for i in range(no):
        el=int(input("Enter the elements of list:"))
        list.append(el)
    return list

def isPrime(x):
    flag=0
    for i in range(2,(x//2)+1):
        if x % i == 0:
            flag=1
            break

    if flag != 1:
        return x

def redFun(no1,no2):
    if no1>no2:
        return no1
    else:
        return no2

def main():
    lst=acceptList()
    print("Entered list is: ",lst)
    filtered=list(filter(isPrime,lst))
    print("Filtered Prime no list:",filtered)
    mapped=list(map(lambda no:no*2,filtered))
    print("Mapped data: ",mapped)
    reduced=reduce(redFun,mapped)
    print("Max is: ",reduced)


if __name__ == '__main__':
    main()