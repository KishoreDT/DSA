import time
n=range(100000)
lt=list(n)
x=int(input("Enter a number to be found :"))
def bs():
    s=time.time()
    l=0
    h=len(lt)-1
    m=0
    while l<=h:
        m=(h+l)//2
        if lt[m]<x:
            l=m+1
            m=m
        elif lt[m]>x:
            h=m-1
            m=m
        else:
            m=m
            if lt[m]==x:
                print("Element Found")
                break
    else:
        print("Element not Found")
    e=time.time()
    print("Time Taken for Bianry Search is",e-s)

def ls():
    s=time.time()
    r=0
    for i in range(0,len(lt)):
        if lt[i]==x:
            r=lt[i]
    if r==x:
        print("Element Found")
    else:
        print("Element not Found")
    e=time.time()
    print("Time Taken for Linear Search is",e-s)

bs()
ls()