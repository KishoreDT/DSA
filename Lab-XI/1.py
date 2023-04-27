import os

COUNT = [10]
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def pt(root):
    if root is not None:
        pt(root.left)
        print(str(root.key) + ",", end=' ')
        pt(root.right)

def insert(node, key):
    if node is None:
        return Node(key)
    if key==node.key:
        print("Repetation Not Allowed")
    else:
        if key < node.key:
            node.left = insert(node.left, key)
        elif key > node.key:
            node.right = insert(node.right, key)
        return node

def min(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current


def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif(key > root.key):
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = min(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

def search(root, key):
    if root is None or root.key == key:
        return True
    if root.key < key:
        return search(root.right,key)
    return search(root.left,key)

def print2DUtil(root, space) :
    if (root == None) :
        return
    space += COUNT[0]
    print2DUtil(root.right, space)
    print()
    for i in range(COUNT[0], space):
        print(end = " ")
    print(root.key)
    print2DUtil(root.left, space)
    
def print2D(root) :
    print2DUtil(root, 0)


root=None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)

while True:
    print("----------------------------------------------------------")
    print("           Binary Search Tree using Linked List")
    print("----------------------------------------------------------")
    print("1. Print \n2. Insert \n3. Delete \n4. Traverse \n5. Search \n6. To clear terminal \n7. Exit")
    ch=int(input("Enter your choice :"))
    print("\n")
    if ch==1:
        print2D(root)
    elif ch==2:
        x=int(input("Enter element to be inserted :"))
        root=insert(root,x)
    elif ch==3:
        key=int(input("Enter element to be deleted :"))
        root=delete(root,key)
    elif ch==4:
        pt(root)
    elif ch==5:
        key=int(input("Enter element to be searched :"))
        x=search(root,key)
        if x==True:
            print("\nElement is there")
        else:
            print("\nElement is not there")
    elif ch==6:
        os.system('cls')
    elif ch==7:
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