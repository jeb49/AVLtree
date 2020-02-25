class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

"""
    implement insert, delete, find next, find prev
    find min and find max recurisivly
"""

def inOrder(n):
    if n:
        inOrder(n.right)
        print(n.data, end = " ")
        inOrder(n.left)

def inOrderArr(n, arr):
    if (n == None):
        return arr
    
    if (n.left):
        inOrderArr(n.left, arr)
    arr.append(n.data)
    if (n.right):
        inOrderArr(n.right, arr)

def findMaxRec(root):
    if root.right == None:
        return root.data
    else:
        return findMaxRec(root.right)

def findMinRec(root):
    if root.left == None:
        return root.data
    else:
        return findMaxRec(root.left)


def findNext(root, n):
    #in order traversal
    arr = []
    inOrderArr(root, arr)
    #not optimal cause im lazy lol
    minNum = findMinRec(root)
    maxNum = findMaxRec(root)

    if (n == minNum or n == maxNum):
        return -1

    return arr[arr.index(n) + 1]

def findPrev(root, n):
    #in order traversal
    arr = []

    inOrderArr(root, arr)
    #not optimal cause im lazy lol
    minNum = findMinRec(root)
    maxNum = findMaxRec(root)

    if (n == minNum or n == maxNum):
        return -1

    return arr[arr.index(n) - 1]

#this is only a helper function to help with debugging to get a visual rep of the tree
def preOrder(self, n):
    if n:
        self.preOrder(n.right)
        print(n.data, end = " ")
        self.preOrder(n.left)

def insertRec(root, num):
    if root == None: 
        root = num
    else:
        if root.data < num.data:
            if root.right == None:
                root.right = num
                # root.right.parent = root
            else:
                insertRec(root.right, num)
        elif root.data > num.data:
            if root.left == None:
                root.left = num
                # root.left.parent = root
            else:
                insertRec(root.left, num)

n = Node(21)
insertRec(n, Node(12))
insertRec(n, Node(30))
insertRec(n, Node(112))

inOrder(n)

print("max", findMaxRec(n))
print("min", findMinRec(n))
print("prev", findPrev(n,30))
print("next", findNext(n,30))