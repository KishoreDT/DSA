import os

class LS():
    def __init__(self):
        self.n = 0
        self.L = []
    
    def __len__(self):
        return self.n
    
    def __getitem__(self, k):
        if not 0 <=k <self.n:
            return IndexError('k is out of bounds')
        return self.L[k]
    
    def pt(self):
        # O(1)
        print(self.L)
    
    def append(self,k):
        # O(1)
        self.L.append(k)
        self.n+=1
    
    def insert(self,p,k):
        # O(1)
        if p==self.n:
            self.L.append(k)
        elif p<self.n and p>=0:
            self.L.insert(p,k)
        else:
            print("It is not a valid position")
        self.n+=1
    
    def locate(self,k):
        # O(n)
        for i in range(0,self.n):
            if k==self.L[i]:
                x=self.L[i]
        if k==x:
            print("The element",k,"found at index",i)
        else:
            print("Element not found")
    
    def reteieve(self,k):
        # O(1)
        print(self.L[k])
    
    def delete(self,k):
        # O(1)
        if k==self.n:
            self.L.pop()
        elif k<self.n and k>0:
            self.L.pop(k)
        else:
            print("It is not a valid position")
        self.n-=1
    def first(self):
        # O(1)
        print(self.L[0])

    def mnull(self):
        # O(1)
        self.L.clear()

    def next(self,k):
        # O(1)
        print(self.L[k+1])
    
    def previous(self,k):
        # O(1)
        print(self.L[k-1])


l = LS()
while True:
    print("----------------------------------------------------------")
    print("                         Array")
    print("----------------------------------------------------------")
    print("1.  Print \n2.  Append \n3.  Locate \n4.  Insert \n5.  Retrieve \n6.  Delete \n7.  Next \n8.  Prervious \n9.  Make Null \n10. First \n11. To Clear Terminal \n12. Exit")
    ch=int(input("Enter your choice :"))
    print("\n")
    if ch==1:
        l.pt()
    elif ch==2:
        x=int(input("Enter a number to be appended :"))
        l.append(x)
    elif ch==3:
        x=int(input("Enter a number to be located :"))
        l.locate(x)
    elif ch==4:
        x=int(input("Enter a position :"))
        y=int(input("Enter a number to be inserted :"))
        l.insert(x,y)
    elif ch==5:
        x=int(input("Enter a position to be reteieve :"))
        l.reteieve(x)
    elif ch==6:
        x=int(input("Enter a position to be deleted :"))
        l.delete(x)
    elif ch==7:
        x=int(input("Enter a position :"))
        l.next(x)
    elif ch==8:
        x=int(input("Enter a position :"))
        l.previous(x)
    elif ch==9:
        l.mnull()
    elif ch==10:
        l.first()
    elif ch==11:
        os.system('cls')
    elif ch==12:
        exit()
    else:
        print("Wrong choice")
    print("\n")