class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

"""
    implement insert, delete, find next, find prev
    find min and find max Iterurisivly
    https://www.youtube.com/watch?v=gcULXE7ViZw
"""
#this is only a helper function to help with debugging to get a visual rep of the tre
def inOrder(n):
    if n:
        inOrder(n.left)
        print(n.data, end = " ")
        inOrder(n.right)

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

def deleteRec(root, num):
    if root == None:
        return root
    elif (num < root.data):
        root.left = deleteRec(root.left, num)
    elif (num > root.data):
        root.right = deleteRec(root.right, num)
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
            temp = findMinRec(root)
            root.data = temp
            root.right = deleteRec(root.right, temp) 
    return root
    
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
print()

print("max", findMaxRec(n))
print("min", findMinRec(n))
print("prev 30", findPrev(n,30))
print("next 30", findNext(n,30))


print("delete 30")
n = deleteRec(n, 30)
inOrder(n)
print()
