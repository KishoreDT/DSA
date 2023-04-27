import os

class Stack:
    def __init__(self,c):
        self.stack = []
        self.front = 0
        self.size = c

    def push(self, element):
        if(self.size == self.front):
            print("\nStack is full")
        else:
            self.stack.append(element)
            self.front += 1

    def pop(self):
        if(not self.isEmpty()):
            lastElement = self.stack[-1]
            del(self.stack[-1])
            return lastElement
        else:
            return("Stack Already Empty")

    def isEmpty(self):
        return self.stack == []

    def pt(self):
        print(self.stack)

n=int(input("Enter the size of Stack :"))
s = Stack(n)
while True:
    print("----------------------------------------------------------")
    print("                         Stack")
    print("----------------------------------------------------------")
    print("1. Print \n2. Push \n3. Pop \n4. To clear terminal \n5. Exit")
    ch=int(input("Enter your choice :"))
    print("\n")
    if ch==1:
        s.pt()
    elif ch==2:
        x=input("Enter the element to be inserted :")
        s.push(x)
    elif ch==3:
        s.pop()
    elif ch==4:
        os.system('cls')
    elif ch==5:
        exit()
    else:
        print("Wrong choice")
    print("\n")