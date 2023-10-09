N=int(input("type the number :"))
if N>0 :
    F=1
    for I in range (2,N+1):
        F=F*I
    print("the number factorial is :",F)
elif N == 0 :
        print("the number factorial is : 1")
else :
    print("please enter a positive number")
