lt=[1,2,3,4,5]
x=int(input("Enter a number to be found :"))
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