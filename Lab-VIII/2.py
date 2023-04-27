import os

COUNT = [10]
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.data
 
    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.data
 
    def delete(self,root, key):
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
            self.deleteDeepest(root,temp)
            key_node.data = x
        return root

    def deleteDeepest(self,root,node_to_delete):
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
            res = self.InorderTraversal(root.left)
            res.append(root.data)
            res = res + self.InorderTraversal(root.right)
        return res

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    def PostorderTraversal(self, root):
        res = []
        if root:
                res = self.PostorderTraversal(root.left)
                res = res + self.PostorderTraversal(root.right)
                res.append(root.data)
        return res
    
    def insert_values(self, data_list):
        for data in data_list:
            self.insert(data)

    def print2DUtil(self, root, space) :
        if (root == None) :
            return
        space += COUNT[0]
        self.print2DUtil(root.right, space)
        print()
        for i in range(COUNT[0], space):
            print(end = " ")
        print(root.data)
        self.print2DUtil(root.left, space)
    
    def print2D(self,root) :
        self.print2DUtil(root, 0)
    
    def height(self, root):
        if root is None:
            return 0 
        leftAns = self.height(root.left)
        rightAns = self.height(root.right)
        return max(leftAns, rightAns) + 1
    
    def findParent(self, root, target):
        if root == None: 
            return False 
        if root.data == target: 
            return True 
        if (self.findParent(root.left, target) or self.findParent(root.right, target)): 
            print(root.data)

root = Node(27)
root.insert_values([14,35,10,19,31,42])
while True:
    print("----------------------------------------------------------")
    print("                      Binary Tree")
    print("----------------------------------------------------------")
    print("1. Print Tree \n2. Insert \n3. Delete \n4. Inorder Traversal \n5. Preorder Traversal \n6. Postorder \n7. To clear terminal \n8. Exit")
    ch=int(input("Enter your choice :"))
    print("\n")
    if ch==1:
        root.print2D(root)
    elif ch==2:
        x=input("Enter the element to be inserted :")
        root.insert(x)
    elif ch==3:
        x=input("Enter the element to be deleted :")
        root.delete(root,x)
    elif ch==4:
        print(root.InorderTraversal(root))
    elif ch==5:
        print(root.PreorderTraversal(root))
    elif ch==6:
        print(root.PostorderTraversal(root))
    elif ch==7:
        print(root.height(root))
    elif ch==8:
        print(root.height(root))
    elif ch==9:
        os.system('cls')
    elif ch==10:
        exit()
    else:
        print("Wrong choice")
    print("\n")
