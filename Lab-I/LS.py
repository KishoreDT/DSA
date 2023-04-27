lt=[1,2,3,4,5]
x=int(input("Enter a number to be found :"))
r=0
for i in range(0,len(lt)):
    if lt[i]==x:
        r=lt[i]
if r==x:
    print("Element Found")
else:
    print("Element not Found")