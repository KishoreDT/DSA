class doubleHashTable:
    def __init__(self):
        self.size = int(input("Enter the Size of the hash table : "))
        self.num = 5
        self.table = list(0 for i in range(self.size))
        self.elementCount = 0
        self.comparisons = 0
   
    def isFull(self):
        if self.elementCount == self.size:
            return True
        else:
            return False
   
    def h1(self, element):
        return element % 10

    def h2(self, element):
        return (3-(element%3))
           
    def doubleHashing(self, element, position):
        posFound = False
        limit = 50
        i = 2
        while i <= limit:
            newPosition = (i*self.h1(element) + self.h2(element)) % self.size
            if self.table[newPosition] == 0:
                posFound = True
                break
            else:
                i += 1
        return posFound, newPosition
 
       
    def insert(self, element):
        if self.isFull():
            print("Hash Table Full")
            return False
        posFound = False
        position = self.h1(element)
        if self.table[position] == 0:
            self.table[position] = element
            print("Element " + str(element) + " at position " + str(position))
            isStored = True
            self.elementCount += 1
        else:
            while not posFound:
                print("Collision has occured for element " + str(element) + " at position " + str(position) + " finding new Position.")
                posFound, position = self.doubleHashing(element, position)
                if posFound:
                    self.table[position] = element
                    self.elementCount += 1
        return posFound          
 
    def remove(self, element):
        position = self.search(element)
        if position is not False:
            self.table[position] = 0
            print("Element " + str(element) + " is Deleted")
            self.elementCount -= 1
        else:
            print("Element is not present in the Hash Table")
        return
       
    def display(self):
        print("\n")
        for i in range(self.size):
            print(str(i) + " = " + str(self.table[i]))
        print("The number of element is the Table are : " + str(self.elementCount))
       
           
table1 = doubleHashTable()
 
table1.insert(22)
table1.insert(32)
table1.insert(45)
table1.insert(67)
table1.insert(89)
table1.insert(9)
 
table1.display()
print()
