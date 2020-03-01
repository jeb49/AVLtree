class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

"""
    implement insert, delete, find next, find prev
    find min and find max 
    source: https://www.techiedelight.com/inorder-tree-traversal-iterative-recursive/
"""



def findMaxIter(root):
    while True:
        if root.right == None:
            return root.data
        else:
            root = root.right

def findMinIter(root):
    while True:
        if root.left == None:
            return root.data
        else:
            root = root.left


def findNext(root, n):
    #in order traversal

    minNum = findMinIter(root)
    maxNum = findMaxIter(root)

    if (n == minNum or n == maxNum):
        return -1

    while True:
        if root.right == None:
            return root.data
        else:
            root = root.right

    # return arr[arr.index(n) + 1]

def findPrev(root, n):
    #in order traversal
    minNum = findMinIter(root)
    maxNum = findMaxIter(root)

    if (n == minNum or n == maxNum):
        return -1

    while True:
        if root.left == None:
            return root.parent.data
        else:
            root = root.left


def insertIter(root, num):
    if root == None: 
        root = num
    else:
        while True:
            if root.data < num.data:
                if root.right == None:
                    root.right = num
                    root.right.parent = root
                    break
                else:
                    root = root.right
            elif root.data > num.data:
                if root.left == None:
                    root.left = num
                    root.left.parent = root
                    break
                else:
                    root = root.left

def inOrder(n):
    if n:
        inOrder(n.left)
        print(n.data, end = " ")
        inOrder(n.right)


def deleteRec(root, num):
    while True:
        if root == None:
            return root
        elif (num < root.data):
            root = root.left
            
        elif (num > root.data):
            root = root.right 
        else:
            if (root.left == None and root.right == None):
                root = None
                return root
            elif (root.left == None):
                temp = root.right
                root = None
                return temp
            elif (root.right == None):
                temp = root.left
                root = None
                return temp
            else:
                temp = findMinIter(root)
                root.data = temp
                num = temp
                root = root.right    
        return root

n = Node(21)
insertIter(n, Node(12))
insertIter(n, Node(30))
insertIter(n, Node(112))

inOrder(n)
print()
print("max", findMaxIter(n))
print("min", findMinIter(n))

print("next 30", findNext(n, 30))
print("prev 30", findPrev(n, 30))

print("delete 30")
n = deleteRec(n, 30)
inOrder(n)
print()
