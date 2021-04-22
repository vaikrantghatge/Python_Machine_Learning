#Write a program which display 10 to 1 on screen.
#Output : 10 9 8 7 6 5 4 3 2 1 

#while loop:-
#def Reverse():
#    iCnt = 10
#    while iCnt > 0:
#	    print(iCnt)
#	    iCnt=iCnt-1

#for loop:-
def Reverse():
    iCnt = 0
    for iCnt in range(10,0,-1):
        print(iCnt, end =" ")

def main():
    Reverse()

if __name__ == "__main__":
	main()