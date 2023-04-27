import time
#n=int(input("Enter a number :"))
n=range(100000)
l=list(n)
st=set(n)
t=tuple(n)
d={}
for i in range(1,1000):
    d[i]=i

#y=int(input("Enter a number to be inserted :"))
def list_insert():
    s=time.time()*1000
    l.append(11)
    e=time.time()*1000
    print("Time Taken for list inserting element is",e-s)
def set_insert():
    s=time.time()*1000
    st.add(11)
    e=time.time()*1000
    print("Time Taken for set inserting element is",e-s)
def list_remove():
    s=time.time()*1000
    l.pop()
    e=time.time()*1000
    print("Time Taken for list removing element is",e-s)
def set_remove():
    s=time.time()*1000
    st.pop()
    e=time.time()*1000
    print("Time Taken for set removing element is",e-s)
def dist_insert():
    s=time.time()*1000
    d[500]=451
    e=time.time()*1000
    print("Time Taken for dist inserting element is",e-s)
def dist_remove():
    s=time.time()*1000
    d.pop(684)
    e=time.time()*1000
    print("Time Taken for dist removing element is",e-s)
def list_max():
    s=time.time()*1000
    max(l)
    e=time.time()*1000
    print("Time Taken for list max element is",e-s)
def set_max():
    s=time.time()*1000
    max(st)
    e=time.time()*1000
    print("Time Taken for set max element is",e-s)
def dist_max():
    s=time.time()*1000
    max(d)
    e=time.time()*1000
    print("Time Taken for dist max element is",e-s)
    
list_insert()
list_remove()
list_max()
print("\n")
set_insert()
set_remove()
set_max()
print("\n")
dist_insert()
dist_remove()
dist_max()