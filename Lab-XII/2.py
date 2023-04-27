import os

class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        root.height = 1 + max(self.height(root.left),self.height(root.right))
        BF = self.bal(root)
        if BF > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if BF < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.min(root.right)
            root.key = temp.key
            root.right = self.delete(root.right,temp.key)
        if root is None:
            return root
        root.height = 1 + max(self.height(root.left),self.height(root.right))
        BF = self.bal(root)
        if BF > 1:
            if self.bal(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if BF < -1:
            if self.bal(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.height(z.left),self.height(z.right))
        y.height = 1 + max(self.height(y.left),self.height(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.height(z.left),self.height(z.right))
        y.height = 1 + max(self.height(y.left),self.height(y.right))
        return y

    def height(self, root):
        if not root:
            return 0
        return root.height

    def bal(self, root):
        if not root:
            return 0
        return self.height(root.left) - self.height(root.right)

    def min(self, root):
        if root is None or root.left is None:
            return root
        return self.min(root.left)

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

def search(root, key):
    if root is None or root.key == key:
        return True
    if root.key < key:
        return search(root.right,key)
    return search(root.left,key)

Tree = AVLTree()
root = None
l = [33, 13, 52, 9, 21, 61, 8, 11]
for k in l:
    root=Tree.insert(root,k)
while True:
    print("----------------------------------------------------------")
    print("                        AVL Tree")
    print("----------------------------------------------------------")
    print("1. Print \n2. Insert \n3. Delete \n4. Search \n5. To clear terminal \n6. Exit")
    ch=int(input("Enter your choice :"))
    print("\n")
    if ch==1:
        Tree.preOrder(root)
    elif ch==2:
        x=int(input("Enter a number :"))
        root=Tree.insert(root,x)
    elif ch==3:
        key=int(input("Enter a number :"))
        root=Tree.delete(root,key)
    elif ch==4:
        key=int(input("Enter String :"))
        print(search(root,key))
    elif ch==5:
        os.system('cls')
    elif ch==6:
        exit()
    else:
        print("Wrong choice")
    print("\n")

'''myTree = AVLTree()
root = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
    root = myTree.insert_node(root, num)
myTree.printHelper(root, "", True)
key = 13
root = myTree.delete_node(root, key)
print("After Deletion: ")
myTree.printHelper(root, "", True)'''