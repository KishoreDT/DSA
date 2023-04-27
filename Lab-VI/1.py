import os

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
	
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
	
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self,data):
        if self.head == None:
            self.head=Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
            self.size += 1
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            self.size -= 1
	
    def top(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("The top element is",self.head.data)
    
    def pt(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            temp=self.head
            Lstr = ''
            while temp:
                Lstr += str(temp.data)+' , ' if temp.next else str(temp.data)
                temp = temp.next
            print(Lstr)
    
    def mnull(self):
        for i in range(self.size+1):
            self.pop()
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.push(data)

#n=int(input("Enter the size of Stack :"))
s = Stack()
s.insert_values(["ASE","CYS","CSE"])
while True:
    print("----------------------------------------------------------")
    print("                  Stack using Linked List")
    print("----------------------------------------------------------")
    print("1. Print \n2. Push \n3. Pop \n4. Top \n5. Null \n6. To clear terminal \n7. Exit")
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
        s.top()
    elif ch==5:
        s.mnull()
    elif ch==6:
        os.system('cls')
    elif ch==7:
        exit()
    else:
        print("Wrong choice")
    print("\n")