import os

class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_last(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)
    
    def search(self, key):
        temp = self.head
        while temp:
            if temp.key == key:
                return temp.key
            else:
                temp = temp.next
    
    def delete(self, key):
        if self.head:
            if self.head.key == key:
                self.head = self.head.next
        else:
            temp = self.head
            while temp.next:
                if temp.next.key == key:
                    temp.next = temp.next.next
                else:
                    temp = temp.next

    def traverse(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp = self.head
        Lstr = ''
        while temp:
            Lstr += str(temp.key)+' , ' if temp.next else str(temp.key)
            temp = temp.next
        print(Lstr)

class HashTable:
    def __init__(self):
        self.capacity = 10
        self.length = 0
        self.buckets = [LinkedList() for i in range(0, self.capacity)]
    
    def len(self):
        return self.length

    def hash(self, key):
        return len(key)%self.capacity
    
    def insert(self, key):
        index = self.hash(key)
        add = self.buckets[index].add_last(key)
        if add == 0:
            self.length += 1
    
    def search(self, key):
        index = self.hash(key)
        return self.buckets[index].search(key)
    
    def delete(self, key):
        index = self.hash(key)
        value = self.buckets[index].delete(key)
        if value:
            self.length -= 1
    
    def traverse(self):
        for i in range(0, self.capacity):
            self.buckets[i].traverse()
    
    def insert_values(self, data_list):
        for data in data_list:
            self.insert(data)

ht = HashTable()
l=["Apple","Cat","Label","Goat","Hall"]
ht.insert_values(l)
while True:
    print("----------------------------------------------------------")
    print("              Hash Table using Linked List")
    print("----------------------------------------------------------")
    print("1. Print \n2. Insert \n3. Delete \n4. Length \n5. Search \n6. To clear terminal \n7. Exit")
    ch=int(input("Enter your choice :"))
    print("\n")
    if ch==1:
        ht.traverse()
    elif ch==2:
        x=input("Enter String :")
        ht.insert(x)
    elif ch==3:
        key=input("Enter String :")
        ht.delete(key)
    elif ch==4:
        print("Length :",ht.len())
    elif ch==5:
        key=input("Enter String :")
        print(ht.search(key))
    elif ch==6:
        os.system('cls')
    elif ch==7:
        exit()
    else:
        print("Wrong choice")
    print("\n")

'''print("Length:", ht.len())
ht.insert("ashton", 99) #add a new item
ht.insert("agar", 87) #add a new item
ht.insert("emily", 90) #add a new item
ht.insert("agar", 89) #update
key = "emily"
print(f"The score of {key} is {ht.search(key)}") #searching score
print(f"The score of deleted item with name/key {key} is {ht.delete(key)}") #deleting item
print("Length:", ht.len())
print("Get all items")
ht.traverse()'''