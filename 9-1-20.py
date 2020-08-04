#TREE'S=====================

'''class Node:
    def __init__(self,data):
        self.left = None
        self.right  = None
        self.data = data
    #INSERTING NODE=========
    def insert(self,data):
        if self.data:
            if data< self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    #Printing Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    #Inorder Traversal
    def inorderTraversal(self,root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res+self.inorderTraversal(root.right)
        return res
    #PREORDER TRAVERSAL
    #root->left->right
    def preorderTraversal(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res+self.preorderTraversal(root.left)
            res = res+self.preorderTraversal(root.right)
        return res
    #POSTORDER TRAVERSAL
    #left->right->root
    def postorderTraversal(self,root):
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            #print(res)
            res = res+self.postorderTraversal(root.right)
            #print(res)
            res.append(root.data)
            #print(res)
            #print()
        return res
    #findval method to compare the value with nodes
    def findval(self,f_v):
        if f_v<self.data:
            if self.left is None:
                return str(f_v)+"Not Found"
            return self.left.findval(f_v)
        elif f_v>self.data:
            if self.right is None:
                return str(f_v)+"Not Found"
            return self.right.findval(f_v)
        else:
            return (str(self.data)+" is found")
    
    
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(31)
root.insert(19)
root.insert(42)
root.PrintTree()
print(root.postorderTraversal(root))
print()
print(root.inorderTraversal(root))
print()
print(root.preorderTraversal(root))
print()
print(root.findval(27))'''


#MERGE SORT

def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i=j=k=0

        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        #Checking if any element was left
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1
        return arr
arr=[12,11,13,5,6,7]
print(mergeSort(arr))
        































        
