#Write a program which display first 10 even numbers on screen.
#Output : 2 4 6 8 10 12 14 16 18 20 

#Range-------------------------------------------
#def DisplayEven():
#    iCnt = 0
#    for iCnt in range(2,22,2):
#        print(iCnt, end =" ")

#Normal------------------------------------------
def DisplayEven():
    iCnt = 1
    while iCnt<=20:
        if iCnt%2==0:
            print(iCnt, end=" ")
        iCnt = iCnt+1

def main():
    DisplayEven()
if __name__ == '__main__':
    main()