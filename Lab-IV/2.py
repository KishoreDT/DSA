import os

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head
    
    def append(self,data):    
        newNode = Node(data);    
        if self.head.data is None:    
            self.head = newNode;    
            self.tail = newNode;    
            newNode.next = self.head;    
        else:    
            self.tail.next = newNode;    
            self.tail = newNode;    
            self.tail.next = self.head;   
    
    def insert(self, data, p):     
        newNode = Node(data)
        temp = self.head
        NoOfElements = 0
        if(temp != None):
            NoOfElements += 1
            temp = temp.next
        while(temp != self.head):
            NoOfElements += 1
            temp = temp.next
        if(p < 1 or p > (NoOfElements+1)):
            print("\nInavalid position.")
        elif (p == 1):
            if(self.head == None):
                self.head = newNode
                self.head.next = self.head
            else:
                while(temp.next != self.head):
                    temp = temp.next
                newNode.next = self.head
                self.head = newNode
                temp.next = self.head
        else:
            temp = self.head
            for i in range(1, p-1):
                temp = temp.next 
            newNode.next = temp.next
            temp.next = newNode

    def delete(self, p):
        nodeToDelete = self.head
        temp = self.head
        NoOfElements = 0
        if(temp != None):
            NoOfElements += 1
            temp = temp.next
        while(temp != self.head):
            NoOfElements += 1
            temp = temp.next
        if(p < 1 or p > NoOfElements):
            print("\nInavalid position.")
        elif (p == 1):
            if(self.head.next == self.head):
                self.head = None
            else:
                while(temp.next != self.head):
                    temp = temp.next
                self.head = self.head.next
                temp.next = self.head
                nodeToDelete = None
        else:
            temp = self.head
            for i in range(1, p-1):
                temp = temp.next 
            nodeToDelete = temp.next
            temp.next = temp.next.next
            nodeToDelete = None

    def insert_values(self, data_list):
        self.head.next = None
        for data in data_list:
            self.append(data)

    def pt(self):
        temp=self.head
        Lstr = ''
        while temp:
            Lstr += str(temp.data)+' , ' if temp.next else str(temp.data)
            temp = temp.next
            if(temp == self.head):
                break
        print(Lstr)

l=CircularLinkedList()
l.insert_values(["ASE","CYS","CSE"])
while True:
    print("----------------------------------------------------------")
    print("                   Circular Linked List")
    print("----------------------------------------------------------")
    print("1. Print \n2. Insert at a given position \n3. Delete at a given position \n4. Traverse \n5. To clear terminal \n6. Exit")
    ch=int(input("Enter your choice :"))
    print("\n")
    if ch==1:
        l.pt()
    elif ch==2:
        x=input("Enter the element to be inserted :")
        y=int(input("Enter the position :"))
        l.insert(x,y)
    elif ch==3:
        x=int(input("Enter the position :"))
        l.delete(x)
    elif ch==4:
        l.pt()
    elif ch==5:
        os.system('cls')
    elif ch==6:
        exit()
    else:
        print("Wrong choice")
    print("\n")