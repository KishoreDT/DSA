import os

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.front == None
	
    def enqueue(self, item):
        temp = Node(item)
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        temp = self.front
        self.front = temp.next
        if(self.front == None):
            self.rear = None
        self.size -= 1
    
    def pt(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            temp=self.front
            Lstr = ''
            while temp:
                Lstr += str(temp.data)+' , ' if temp.next else str(temp.data)
                temp = temp.next
            print(Lstr)
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.enqueue(data)

#n=int(input("Enter the size of Queue :"))
q = Queue()
q.insert_values(["ASE","CYS","CSE"])
while True:
    print("----------------------------------------------------------")
    print("                  Queue using Linked List")
    print("----------------------------------------------------------")
    print("1. Print \n2. Enqueue \n3. Dequeue \n4. To clear terminal \n5. Exit")
    ch=int(input("Enter your choice :"))
    print("\n")
    if ch==1:
        q.pt()
    elif ch==2:
        x=input("Enter the element to be inserted :")
        q.enqueue(x)
    elif ch==3:
        q.dequeue()
    elif ch==4:
        os.system('cls')
    elif ch==5:
        exit()
    else:
        print("Wrong choice")
    print("\n")