class PriorityQueueNode:
    def __init__(self, value):
        self.data = value
        self.next = None

class PriorityQueue:
	def __init__(self):
		self.front = None

	def isEmpty(self):
		return True if self.front == None else False

	def enqueue(self, value):
		if self.isEmpty() == True:
			self.front = PriorityQueueNode(value)
			
		else:
			if self.front.data < value:
				newNode = PriorityQueueNode(value)
				newNode.next = self.front
				self.front = newNode
			else:
				temp = self.front
				while temp.next:
					if value >= temp.next.data:
						break
					temp = temp.next
				newNode = PriorityQueueNode(value)
				newNode.next = temp.next
				temp.next = newNode

	def dequeue(self):
		if self.isEmpty() == True:
			return
		else:
			self.front = self.front.next
			return 1

	def peek(self):
		if self.isEmpty() == True:
			return
		else:
			return self.front.data

	def traverse(self):
		if self.isEmpty() == True:
			print("Queue is Empty!")
		else:
			temp = self.front
			while temp:
				print(temp.data, end = " ")
				temp = temp.next

pq = PriorityQueue()
pq.enqueue(85)
pq.enqueue(25)
pq.enqueue(50)
pq.enqueue(39)
print("Queue :")
pq.traverse()
pq.dequeue()
print("\nAfter dequeue :")
pq.traverse()