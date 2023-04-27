import os

class Queue:
	def __init__(self, c):
		self.queue = []
		self.front = self.rear = 0
		self.size = c

	def enqueue(self, data):
		if(self.size == self.rear):
			print("\nQueue is full")
		self.queue.append(data)
		self.rear += 1

	def dequeue(self):
		if(self.front == self.rear):
			print("Queue is empty")
		else:
			self.queue.pop(0)
			self.rear -= 1

	def pt(self):
		if(self.front == self.rear):
			print("\nQueue is Empty")
		for i in self.queue:
			print(i, "<--", end = ' ')

n=int(input("Enter the size of Queue :"))
q = Queue(n)
while True:
    print("----------------------------------------------------------")
    print("                         Queue")
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