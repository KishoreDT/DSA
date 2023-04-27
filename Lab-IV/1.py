import os

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
  
    def add_first(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head != None:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None


    def add_last(self, new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail
        if self.tail == None:
            self.head = new_node 
            self.tail = new_node
            new_node.next = None
        else:
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node

    def remove_first(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
            return temp.data
    
    def remove_last(self):
        if self.tail == None:
            print("List is empty")
        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None
            return temp.data

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.add_last(data)
    
    def insert(self, data, p):
        newNode = Node(data)
        if(p < 1):
            print("\nPosition should be >= 1.")
        elif (p == 1):
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        else:
            temp = self.head
            for i in range(1, p-1):
                if(temp != None):
                    temp = temp.next   
            if(temp != None):
                newNode.next = temp.next
                newNode.prev = temp
                temp.next = newNode  
                if (newNode.next != None):
                    newNode.next.prev = newNode
            else:
                print("\nThe previous node is null.")

    def delete(self, p):
        if(p < 1):
            print("\nPosition should be >= 1.")
        elif (p == 1 and self.head != None):
            nodeToDelete = self.head
            self.head = self.head.next
            nodeToDelete = None
            if (self.head != None):
                self.head.prev = None
        else:    
            temp = self.head
            for i in range(1, p-1):
                if(temp != None):
                    temp = temp.next   
            if(temp != None and temp.next != None):
                nodeToDelete = temp.next
                temp.next = temp.next.next
                if(temp.next.next != None):
                    temp.next.next.prev = temp.next  
                nodeToDelete = None 
            else:
                print("\nThe node is already null.")
    
    def pt(self):
        temp=self.head
        Lstr = ''
        while temp:
            Lstr += str(temp.data)+' , ' if temp.next else str(temp.data)
            temp = temp.next
        print(Lstr)

    def ptf(self):
        print("\nTraversal in forward direction")
        temp=self.head
        Lstr = ''
        while temp:
            Lstr += str(temp.data)+' , ' if temp.next else str(temp.data)
            temp = temp.next
        print(Lstr)
    
    def ptb(self):
        print("\nTraversal in reverse direction")
        temp=self.head
        while temp:
            last = temp
            temp = temp.next
        Lstr = ''
        while last:
            Lstr += ' , '+str(last.data) if last.next else str(last.data)
            last = last.prev
        print(Lstr)

l=DoublyLinkedList()
l.insert_values(["ASE","CYS","CSE"])
while True:
    print("----------------------------------------------------------")
    print("                    Doubly Linked List")
    print("----------------------------------------------------------")
    print("1.  Print \n2.  Insert at beginning \n3.  Insert at end \n4.  Insert at a given position \n5.  Delete at the beginning \n6.  Delete at the end \n7.  Delete at a given position \n8.  Traverse the linked list in forward direction \n9.  Traverse the linked list in backward direction \n10. To clear terminal \n11. Exit")
    ch=int(input("Enter your choice :"))
    print("\n")
    if ch==1:
        l.pt()
    elif ch==2:
        x=input("Enter the element to be inserted :")
        l.add_first(x)
    elif ch==3:
        x=input("Enter the element to be inserted :")
        l.add_last(x)
    elif ch==4:
        x=input("Enter the element to be inserted :")
        y=int(input("Enter the position :"))
        l.insert(x,y)
    elif ch==5:
        l.remove_first()
    elif ch==6:
        l.remove_last()
    elif ch==7:
        x=int(input("Enter the position :"))
        l.delete(x)
    elif ch==8:
        l.ptf()
    elif ch==9:
        l.ptb()
    elif ch==10:
        os.system('cls')
    elif ch==11:
        exit()
    else:
        print("Wrong choice")
    print("\n")