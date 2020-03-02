import random
class Node:
    def __init__(self, data):
        self.data = data
        self.height = 0
        self.left = None
        self.right = None
        self.parent = 0
        self.parent = None

"""
    implement insert, delete, find next, find prev
    find min and find max 
    source: https://www.techiedelight.com/inorder-tree-traversal-iterative-recursive/
"""

def getRandomArray(n):
    arr = []
    for i in range(n):
        #check for no repeats
        while True:
            num = random.randint(0,1000)
            if num in arr:
                num = random.randint(0,1000)
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
    minNum = findMinIter(root)
    maxNum = findMaxIter(root)

    if (n == minNum or n == maxNum):
        return -1

    while True:
        if root.left == None:
            return findMinIter(root.right)
        else:
            root = root.right

def findPrev(root, n):
    minNum = findMinIter(root)
    maxNum = findMaxIter(root)

    if (n == minNum or n == maxNum):
        return -1

    while True:
        if root.left == None:
            return root.parent.data
        else:
            root = root.left
    
#not being used...  yet
def setHeight(root):
    n = root
    lHeight = 0
    rHeight = 0

    if n.left:
        lHeight = n.left.height
    if n.right:
        rHeight = n.right.height
    
    n.height = max(lHeight, rHeight) + 1

def rotateLeft(root):
    leftChild = root.left
    rightChild = root.right

    root.right = leftChild
    leftChild = root

    if leftChild != None:
        leftChild.parent = root
    
    rightChild.parent = root.parent
    root.parent = rightChild

def rotateRight(root):
    leftChild = root.left
    rightChild = root.right

    root.left = rightChild
    rightChold = root

    if rightChild != None:
        rightChild.parent = root
        
    leftChild.parent = root.parent
    root.parent = leftChild

"""
def checkBalanceRec(root):
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
    else:
        if leftBal <= 0:
            #single rotate right
        else:
            #rotate left
            #rotate right
    if rightBal <= 0:
            #single rotate left
        else:
            #rotate right
            #rotate left 
"""

def updateHeight(root):
    lHeight = 0
    rHeight = 0

    if root.left:
        lHeight = root.left.height

    if root.right:
        rHeight = root.right.height
    
    root.height = 1 + max(lHeight, rHeight)

def checkBalanceIter(root):    
    #nodes to keep track of tree
    curr = root
    prev = None
    prevPrev = None

    grandpa = None
    parent = None

    lHeight = 0 
    rHeight = 0 

    #finding grandpa and parent 
    #when the grandpaBF is between -1 and 1 we dont have to do a rotate
    #else we will 

    while True: 
        if root == None:
            break

        lheight = 0 
        rheight = 0 

        if root.left:
            lHeight = root.left.height
        if root.right:
            rHeight = root.right.height
        
        bal = lheight - rHeight 
        # print(root.data)
        # print(bal)

        if  bal >= -1 and bal <= 1:
            grandpa = curr
            parent = prev
            root = prevPrev
            break

        elif curr.parent != None:
            curr = curr.parent
            prevPrev = prev
            prev = root
        else:
            break

    #getting bfs of parent and grandpa

    #if we didnt find anything we finish our function
    if grandpa == None or parent == None:
        return None

    # print(parent.data)
    print("GOT EM")

    grandpaLeft = 0 
    grandpaRight = 0
    if grandpa.left != None:
        grandpaLeft = grandpa.left.height
    if grandpa.right != None:
        grandpaRight = grandpa.right.height

    grandpaBF = grandpaLeft - grandpaRight

    parentLeft = 0 
    parentRight = 0
    if parent.left != None:
        parentLeft = parent.left.height
    if parent.right != None:
        parentRight = parent.right.height

    parentBF = parentLeft - parentRight

    if grandpaBF > 1:
        if parentBF < 0:
            #left Right
            rotateLeft(parent)
            rotateRight(grandpa)
        else:
            #left left
            rotateLeft(parent)
    else:
        if parentBF > 0:
            #right left
            rotateRight(parent)
            rotateLeft(grandpa)
        else: 
            #right right
            rotateRight(parent)
    
    setHeight(root)
    setHeight(parent)
    setHeight(grandpa)
    

def insertIter(root, num):
    if root == None: 
        root = num
    else:
        while True:
            if root.data < num.data:
                if root.right == None:
                    root.right = num
                    root.right.parent = root
                    setHeight(root)
                    checkBalanceIter(root)
                    break
                else:
                    root = root.right
            elif root.data > num.data:
                if root.left == None:
                    root.left = num
                    root.left.parent = root
                    setHeight(root)
                    checkBalanceIter(root)
                    break
                else:
                    root = root.left

def inOrder(n):
    if n:
        inOrder(n.left)
        print(n.data, end = " ")
        inOrder(n.right)


def deleteIter(root, num):
    while True:
        if root == None:
            return root

        elif (num < root.data):
            root = root.left
            # root.parent = root.left.parent
        elif (num > root.data):
            root = root.right
            # root.parent = root.right.parent
        else:
            if (root.left == None and root.right == None):
                root = None
                break
            elif (root.left == None):
                temp = root.right
                #root = None
                root.parent.right = temp
                break
                # return root
            elif (root.right == None):
                temp = root.left
                root.parent.right = temp
                root = None
                break
                # return root
            else:
                temp = findNext(root, root.data)
                root.data = temp
                num = temp
                root = root.right
                continue    
    # return root

n = Node(21)
insertIter(n, Node(12))
insertIter(n, Node(30))
insertIter(n, Node(112))
insertIter(n, Node(55))
insertIter(n, Node(33))
insertIter(n, Node(102))

inOrder(n)
print()
print("max", findMaxIter(n))
print("min", findMinIter(n))

print("next 30", findNext(n, 30))
print("prev 30", findPrev(n, 30))

print("delete 30")
deleteIter(n, 30)


inOrder(n)
print()
