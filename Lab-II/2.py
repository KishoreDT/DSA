import os
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def pt(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp = self.head
        Lstr = ''
        while temp:
            Lstr += str(temp.data)+' , ' if temp.next else str(temp.data)
            temp = temp.next
        print(Lstr)
    
    def add_first(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def add_last(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data, None)
    
    def remove_first(self):
        self.head = self.head.next
        return
    
    def remove_last(self):
        if(self.head != None):
            if(self.head.next == None):
                self.head = None
            else:
                temp = self.head
                while(temp.next.next != None):
                    temp = temp.next
                lastNode = temp.next
                temp.next = None
                lastNode = None
    
    def insert(self, data, p):
        newNode = Node(data)
        if(p < 1):
            print("\np should be >= 1.")
        elif (p == 1):
            newNode.next = self.head
            self.head = newNode
        else:    
            temp = self.head
            for i in range(1, p-1):
                if(temp != None):
                    temp = temp.next
            if(temp != None):
                newNode.next = temp.next
                temp.next = newNode  
            else:
                print("\nThe previous node is null.")
    def delete(self, p):
        if self.head is None:
            return
        temp = self.head
        if p == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(p - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next
    
    def locate(self, data):
        current = self.head
        while current != None:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.add_last(data)

l = LinkedList()
l.insert_values(["CSE","CYS","AI","ML"])
while True:
    print("----------------------------------------------------------")
    print("                       Linked List")
    print("----------------------------------------------------------")
    print("1.  Print the List \n2.  To Insert Element at the Beginning \n3.  To Insert Element at the End \n4.  To Delete Element at the Beginning \n5.  To Delete Element at the End \n6.  To Insert Element at given Position \n7.  To Delete Element at given Position \n8.  To Locate Element in Linked List \n9.  To Clear Terminal \n10. Exit")
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
        l.remove_first()
    elif ch==5:
        l.remove_last()
    elif ch==6:
        x=input("Enter the element to be inserted :")
        y=int(input("Enter the position :"))
        l.insert(x,y)
    elif ch==7:
        x=int(input("Enter the position :"))
        l.delete(x)
    elif ch==8:
        x=input("Enter the element to locate :")
        if l.locate(x):
            print("Element Found")
        else:
            print("Element not Found")
    elif ch==9:
        exit()
    elif ch==10:
        exit()
    else:
        print("Wrong choice")
    print("\n")