#Write a program which accept name from user and display length of its name.
#Input : Marvellous Output : 10 

#LB_Logic:----------------------------------
Using while loop:-
def CheckLength(string):
    iCnt = 0;
    while string[iCnt:]:
        iCnt += 1 
    return iCnt
#-------------------------------
#Using for loop:-
#def CheckLength(string):
#    iCnt = 0;
#    for i in string:
#        iCnt += 1
#    return iCnt
#def main():
#    print("Enter Input",end=" ")
#    value = input()
#    iRet = CheckLength(value)
#    print(iRet,end =" ")

#==========================================
#Using inbuild method:-
#def main():
#    print("Enter Input",end=" ")
#    value = input()
#    print(len(value))
#Using join and count method:-
#def CheckLength(string):
#    if not string:
#        return 0
#    else:
#        return((string).join(string)).count(string) + 1    

def main():
    print("Enter Input",end=" ")
    value = input()
    iRet = CheckLength(value)
    print(iRet,end =" ")

if __name__ == '__main__':
    main()