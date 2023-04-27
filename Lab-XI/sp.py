import os

COUNT = [10]
class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.data == data:
            return False

        elif data < self.data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def minValueNode(self, node):
        current = node
        while(current.leftChild is not None):
            current = current.leftChild

        return current

    def maxValueNode(self, node):
        current = node
        while(current.rightChild is not None):
            current = current.rightChild

        return current


    def delete(self, data,root):
        if self is None:
            return None
        if data < self.data:
            self.leftChild = self.leftChild.delete(data,root)
        elif data > self.data:
            self.rightChild = self.rightChild.delete(data,root)
        else:
            if self.leftChild is None:

                if self == root:
                    temp = self.minValueNode(self.rightChild)
                    self.data = temp.data
                    self.rightChild = self.rightChild.delete(temp.data,root) 

                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:

                if self == root:
                    temp = self.maxValueNode(self.leftChild)
                    self.data = temp.data
                    self.leftChild = self.leftChild.delete(temp.data,root) 

                temp = self.leftChild
                self = None
                return temp
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data,root)

        return self

    def find(self, data):
        if(data == self.data):
            return "data found"
        elif(data < self.data):
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return "data not found"
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return "data not found"

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data), end = ' ')
            if self.rightChild:
                self.rightChild.inorder()

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data,self.root)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return "data not found"

    def inorder(self):
        print()
        if self.root is not None:
            print('Inorder: ')
            self.root.inorder()
bst=Tree()
while True:
    print("----------------------------------------------------------")
    print("           Binary Search Tree using Linked List")
    print("----------------------------------------------------------")
    print("1. Print \n2. Insert \n3. Delete \n4. Search \n5. To clear terminal \n6. Exit")
    ch=int(input("Enter your choice :"))
    print("\n")
    if ch==1:
        bst.inorder()
    elif ch==2:
        x=int(input("Enter element to be inserted :"))
        bst.insert(x)
    elif ch==3:
        key=int(input("Enter element to be deleted :"))
        bst.delete(key)
    elif ch==4:
        key=int(input("Enter element to be searched :"))
        bst.find(key)
    elif ch==5:
        os.system('cls')
    elif ch==6:
        exit()
    else:
        print("Wrong choice")
    print("\n")

'''root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=' ')
inorder(root)

print("\nDelete 10")
root = deleteNode(root, 10)
print("Inorder traversal: ", end=' ')
inorder(root)'''