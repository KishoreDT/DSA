import ctypes
class DynamicArray():
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
    def __len__(self):
        return self.n
    def __getitem__(self, k):
        if not 0 <=k <self.n:
            return IndexError('k is out of bounds')
        return self.A[k]
    def insert(self,p,k):
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.A[p] = k
        self.n += 1
    def locate(self,k):
        for i in range(0,self.n):
            if k==self.A[i]:
                x=self.A[i]
        if k==x:
            print("The element",k,"found at index",i)
        else:
            print("Element not found")
    def reteieve(self):
        print(self.A[self.n-1])
    def append(self, element):
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n] = element
        self.n += 1
    def _resize(self, new_cap):
        B = self.make_array(new_cap)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_cap
    def make_array(self,new_cap):
        return (new_cap * ctypes.py_object)()
arr = DynamicArray()
arr.append(1)
arr.append(2)
print(arr[0])
print(arr[1])
arr.locate(2)
arr.insert(2,4)
print(arr[2])
