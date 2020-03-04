import math
import random
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
#taken from geeksForGeeks 
COUNT = [5]  


def print2DUtil(root, space) : 
  
    # Base case  
    if (root == None) : 
        return
  
    # Increase distance between levels  
    space += COUNT[0] 
  
    # Process right child first  
    print2DUtil(root.right, space)  
  
    # Print current node after space  
    # count  
    print()  
    for i in range(COUNT[0], space): 
        print(end = " ")  
    print(root.data)  
  
    # Process left child  
    print2DUtil(root.left, space)  
  
# Wrapper over print2DUtil()  
def print2D(root) : 
      
    # space=[0] 
    # Pass initial space count as 0  
    print2DUtil(root, 0)  


#this is only a helper function to help with debugging to get a visual rep of the tre
def inOrder(n):
    if n:
        inOrder(n.left)
        print(n.data, end = " ")
        inOrder(n.right)

def getRandomArray(n):
    arr = []
    for i in range(n):
        #check for no repeats
        while True:
            num = random.randint(0, n*1000)
            if num in arr:
                num = random.randint(0, n*1000)
            elif num not in arr:
                break
        arr.append(num)
    return arr

def getSortedArray(n):
    arr = []
    for i in range(n):
        num = n - i
        arr.append(num)
    return arr
    
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

def getHeight(root):
    if root == None:
        return -1
    else:
        return max(getHeight(root.left), getHeight(root.right)) + 1

"""
def rotateLeft(root):
    leftChild = root.left
    rightChild = root.right
    curr = root

    root.right = leftChild
    root.right.left = curr

    if leftChild != None
        root.left.parent = curr
    
    root.right.parent = curr.parent
    root.parent = rightChild

def rotateRight(root):
    leftChild = root.left
    rightChild = root.right
    curr = root

    root.left = rightChild
    root.left.right = curr

    if rightChild != None
        root.right.parent = curr
    
    root.left.parent = curr.parent
    root.parent = leftChild

def checkBalance(root):
    if root == None:
        pass

    leftH = getHeight(root.left)
    rightH = getHeight(root.right)

    bal = leftH - rightH

    leftBal = max(getHeight(leftChild.left), getHeight(leftChild.right))
    rightBal = max(getHeight(rightChild.left), getHeight(rightChild.right))

    if abs(bal) > 1:
        #do nothing because we know that the tree is balanced
        pass
    elif bal < 0:
        if leftBal <= 0:
            #rotate right
        else:
            #rotate left
            #rotate right
    else:   
        if rightBal <= 0:
            #rotate left
        else:
            #rotate right
            #rotate left 
    
    if parent != null:
        checkBalance(root.parent)
    elif rightBal > leftBal:
        checkBalance(root.right)
    else:
        checkBalance(root.left)

"""

def deleteRec(root, num):
    if root == None:
        return root
    elif (num < root.data):
        root.left = deleteRec(root.left, num)
        #balance node
    elif (num > root.data):
        root.right = deleteRec(root.right, num)
        #balance node
    else:
        if (root.left == None and root.right == None):
            root = None
            return root
        elif (root.left == None):
            temp = root.right
            temp.parent = root.right.parent
            root = None
            #balance node
            return temp
        elif (root.right == None):
            temp = root.left
            temp.parent = root.left.parent
            root = None
            #balance node
            return temp
        else:
            temp = findNext(root, root.data)
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
                root.right.parent = root
                #balance
            else:
                insertRec(root.right, num)
        elif root.data > num.data:
            if root.left == None:
                root.left = num
                root.left.parent = root
                #balance
            else:
                insertRec(root.left, num)

n = Node(21)
# insertRec(n, Node(12))
# insertRec(n, Node(30))
# insertRec(n, Node(112))
# insertRec(n, Node(55))
# insertRec(n, Node(33))
# insertRec(n, Node(102))

# print2D(n)
print('\n')

arr = getRandomArray(10000)
# arr = getSortedArray(10000)

for el in arr:
    insertRec(n, Node(el))

# print("max", findMaxRec(n))
# print("min", findMinRec(n))
# print("prev 30", findPrev(n,30))
# print("next 30", findNext(n,30))

print("height", getHeight(n))

# print("delete 30")
# n = deleteRec(n, 30)
# print("delete 12")
# n = deleteRec(n, 12)
# print("delete 112")
# n = deleteRec(n, 112)

inOrder(n)
print("\n")
print("height", getHeight(n))
