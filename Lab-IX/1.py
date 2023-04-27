class PriorityQueue(object):
    def __init__(self):
        self.queue = []
        self.capacity = 10
        self.size = 0
   
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def enqueue(self, data):
        if self.size == self.capacity:
            print("Queue is full!")
        else:
            self.queue.append(data)
            self.size += 1
    
    def dequeue(self):
        if self.isEmpty() == True:
            print("It is Empty")
        else:
            try:
                max = 0
                for i in range(len(self.queue)):
                    if self.queue[i] > self.queue[max]:
                        max = i
                    item = self.queue[max]
                del self.queue[max]
                return item
            except IndexError:
                print()
                exit()

pq = PriorityQueue()
pq.enqueue(85)
pq.enqueue(25)
pq.enqueue(50)
pq.enqueue(39)
print(pq)			
while not pq.isEmpty():
    print(pq.dequeue())
