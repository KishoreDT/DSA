import os

COUNT = [5]
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if root.data == data:
            return root
        elif root.data < data:
            root.right = insert(root.right, data)
        else:
            root.left = insert(root.left, data)
    return root

def insert_values(arr,root,i,n):
    if i<n:
        temp=Node(arr[i])
        root=temp
        root.left=insert_values(arr,root.left,2*i+1,n)
        root.right=insert_values(arr,root.right,2*i+2,n)
        return root

def delete(root, key):
    if root == None :
        return None
    if root.left == None and root.right == None:
        if root.key == key :
            return None
        else :
            return root
    key_node = None
    t = []
    t.append(root)
    temp = None
    while(len(t)):
        temp = t.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            t.append(temp.left)
        if temp.right:
            t.append(temp.right)
    if key_node :
        x = temp.data
        deleteDeepest(root,temp)
        key_node.data = x
    return root

def deleteDeepest(root,node_to_delete):
    t = []
    t.append(root)
    while(len(t)):
        temp = t.pop(0)
        if temp is node_to_delete:
            temp = None
            return
        if temp.right:
            if temp.right is node_to_delete:
                temp.right = None
                return
            else:
                t.append(temp.right)
        if temp.left:
            if temp.left is node_to_delete:
                temp.left = None
                return
            else:
                t.append(temp.left)

def InorderTraversal(self, root):
    res = []
    if root:
        res = InorderTraversal(root.left)
        res.append(root.data)
        res = res + InorderTraversal(root.right)
    return res

def PostorderTraversal(root):
    res = []
    if root:
        res = PostorderTraversal(root.left)
        res = res + PostorderTraversal(root.right)
        res.append(root.data)
    return res

def PreorderTraversal(root):
    res = []
    if root:
        res.append(root.data)
        res = res + PreorderTraversal(root.left)
        res = res + PreorderTraversal(root.right)
    return res

def height(root):
    if root is None:
        return 0 
    leftAns = height(root.left)
    rightAns = height(root.right)
    return max(leftAns, rightAns) + 1

def findParent(root, target):
    if root == None: 
        return False 
    if root.data == target: 
        return True 
    if (findParent(root.left, target) or findParent(root.right, target)): 
        print(root.data)

def print2DUtil(root, space) :
    if (root == None) :
        return
    space += COUNT[0]
    print2DUtil(root.right, space)
    print()
    for i in range(COUNT[0], space):
        print(end = " ")
    print(root.data)
    print2DUtil(root.left, space)
    
def print2D(root) :
    print2DUtil(root, 0)

'''if __name__ == "__main__":
    arr=[1000,100,200,300,400,500,600]
    n=len(arr)
    root = None 
    root=insert(arr,root,0,n)
    print("Height of the tree :",height(root))
    print("\nThe values in the binary tree are... (Pre-order traversal)")
    print(PreorderTraversal(root))
    print("\nThe values in the binary tree are... (Post-order traversal)")
    print(PostorderTraversal(root))
    root = delete(root, 200)
    print("\n\nThe values in the binary tree after deleting '200' are... (Post-order traversal)")
    print(PostorderTraversal(root))
    print("\n")
    x=int(input("Enter the element to find parent :"))
    a=findParent(root,x)
    if a==True:
        print("Root Node, No Parent")'''

arr=[1000,100,200,300,400,500,600]
n=len(arr)
root = None 
root=insert_values(arr,root,0,n)
while True:
    print("----------------------------------------------------------")
    print("                      Binary Tree")
    print("----------------------------------------------------------")
    print("1.  Print Tree \n2.  Insert \n3.  Delete \n4.  Inorder Traversal \n5.  Preorder Traversal \n6.  Postorder Traversal \n7.  Height \n8.  Parent \n9.  To clear terminal \n10. Exit")
    ch=int(input("Enter your choice :"))
    print("\n")
    if ch==1:
        print2D(root)
    elif ch==2:
        x=input("Enter the element to be inserted :")
        insert(root,x)
    elif ch==3:
        x=input("Enter the element to be deleted :")
        delete(root,x)
    elif ch==4:
        print(InorderTraversal(root))
    elif ch==5:
        print(PreorderTraversal(root))
    elif ch==6:
        print(PostorderTraversal(root))
    elif ch==7:
        print(height(root))
    elif ch==8:
        x=int(input("Enter the element to find parent :"))
        print("\n")
        a=findParent(root,x)
        if a==True:
            print("Root Node, No Parent")
    elif ch==9:
        os.system('cls')
    elif ch==10:
        exit()
    else:
        print("Wrong choice")
    print("\n")
