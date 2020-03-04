import random
class Node:
    def __init__(self, data):
        self.data = data
        self.height = 1
        self.left = None
        self.right = None
        self.parent = None

"""
    implement insert, delete, find next, find prev
    find min and find max 
    source: https://www.techiedelight.com/inorder-tree-traversal-iterative-recursive/
"""

#taken from geeksForGeeks 
COUNT = [10]  


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

def findMaxIter(root):
    while True:
        if root.right == None:
            return root.data
        else:
            if root.left != None:
                root = root.left
            else:
                return root.data

def findMinIter(root):
    while True:
        if root.left == None:
            return root.data
        else:
            if root.left != None:
                root = root.left
            else:
                return root.data


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
    
def rotateLeft(root):
    leftChild = root.left
    rightChild = root.right
    
    if rightChild != None:
        temp = rightChild.left 
    else:
        temp = None

    root.right = temp
    
    if rightChild != None:
        rightChild.parent = root.parent
    rightChild.left = root
    root.parent = rightChild

    if temp != None:
        temp.parent = root

    return rightChild

def rotateRight(root):
    leftChild = root.left
    rightChild = root.right

    if leftChild != None: 
        temp = leftChild.right 
    else:
        temp = None

    root.left = temp

    print("AAAAAAAAAAHHHHHHHHHHHHHH")
    # print(leftChild)
    # print(leftChild.parent)
    # print(root.parent)

    if leftChild != None:
        leftChild.parent = root.parent
    leftChild.right = root
    root.parent = leftChild

    if temp != None:
        temp.parent = root

    return leftChild


def setHeight(root):
    if root == None:
        return 0

    while True:
        lHeight = 0
        rHeight = 0


        if root.left != None:
            lHeight = root.left.height

        if root.right != None:
            rHeight = root.right.height

        root.height = 1 + max(lHeight, rHeight)

        #updating ancestors
        if root.parent != None:
            root = root.parent
        elif root.parent == None:
            break

def checkBF(root):
    if root == None:
        return None

    if root.left != None:
        leftHeight = root.left.height
    else:
        leftHeight = 0 

    if root.right != None:
        rightHeight = root.right.height
    else:
        rightHeight = 0

    bal = leftHeight - rightHeight
    print('root', root.data, 'height', root.height)
    print('left height', leftHeight, 'right height', rightHeight)
    return bal

def balanceIter(root, oldestBf):    
    oldest = root
    temp =  oldest.parent

    if oldestBf > 1:    
        middle = root.left
        youngest = root.left.left
        middleBf = checkBF(middle)
        # youngest = checkBF(youngest)

        if middleBf < 0: 
            root.left = rotateLeft(middle)
            root = rotateRight(root)
        else:
            root = rotateRight(oldest)

        if temp:
            if temp.left and temp.left == oldest:
                temp.left = root
            else:
                temp.right = root

        setHeight(oldest)
        setHeight(middle)
        setHeight(youngest)

    elif oldestBf < -1:    
        middle = root.right
        youngest = root.right.left
        middleBf = checkBF(root.right)

        if middleBf > 0: 
            print("rightLeft")
            root.right = rotateRight(middle)
            root = rotateLeft(oldest)
        else:
            print("Left")
            root = rotateLeft(oldest)
        
        if temp:
            if temp.left and temp.left == oldest:
                temp.left = root
            else:
                temp.right = root
            
        setHeight(oldest)
        setHeight(middle)
        setHeight(youngest)
    

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

                    #inserting all the ancenstors
                    parentArr = []
                    node = root.right

                    while True:
                        if node.parent != None:
                            bal = checkBF(node.parent)
                            if bal > 1 or bal < -1:
                                print('i did it')
                                balanceIter(node.parent, bal)

                            #check if parent exists
                            if node.parent != None:
                                node = node.parent
                            else:
                                break
                        else:
                            break
                    break
                else:
                    root = root.right

            elif root.data > num.data:
                if root.left == None:
                    root.left = num
                    root.left.parent = root
                    setHeight(root)

                    node = root.left

                    while True:
                        if node.parent != None:
                            bal = checkBF(node.parent)
                            if bal > 1 or bal < -1:
                                print('i did it')
                                balanceIter(node.parent, bal)
                            
                            #check if parent exists 
                            if node.parent != None:
                                node = node.parent
                            else:
                                break
                        else:
                            break
                    break
                else:
                    root = root.left                 
    return node

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

                if root.parent != None:
                    root.parent.right = temp

                root = None

                node = temp

                while True:
                    if node.parent != None:
                        bal = checkBF(node.parent)
                        if bal > 1 or bal < -1:
                            print('i did it')
                            balanceIter(node.parent, bal)

                        #check if parent exists
                        if node.parent != None:
                            node = node.parent
                        else:
                            break
                    else:
                        break

                break
                # return root
            elif (root.right == None):
                temp = root.left

                if root.parent != None:
                    root.parent.left = temp
                root = None

                node = temp

                while True:
                    if node.parent != None:
                        bal = checkBF(node.parent)
                        if bal > 1 or bal < -1:
                            print('i did it')
                            balanceIter(node.parent, bal)

                        #check if parent exists
                        if node.parent != None:
                            node = node.parent
                        else:
                            break
                    else:
                        break

                break
                # return root
            else:
                temp = findMinIter(root)
                root.data = temp
                num = temp
                root = root.right
    return node

n = Node(21)

# testing rotate
# n.left = Node(5)
# n.right = Node(30)
# n.right.left = Node(25)

# print2D(n)
# n = rotateLeft(n)
# print2D(n)


# testing insert, the dashes are there so i can visually rep the tree
insertIter(n, Node(12))
print('---------------------------------------------------------\n\n\n---------------------------------------------------------')
print2D(n)
n = insertIter(n, Node(30))
print('---------------------------------------------------------\n\n\n---------------------------------------------------------')
print2D(n)
n = insertIter(n, Node(112))
print('---------------------------------------------------------\n\n\n---------------------------------------------------------')
print2D(n)
n = insertIter(n, Node(55))
print('---------------------------------------------------------\n\n\n---------------------------------------------------------')
print2D(n)
n = insertIter(n, Node(33))
print('---------------------------------------------------------\n\n\n---------------------------------------------------------')
print2D(n)
n = insertIter(n, Node(102))
print('---------------------------------------------------------\n\n\n---------------------------------------------------------')
print2D(n)

print('\n')
print('\n')


# nums = getRandomArray(10000)
# print('we are good')

# for el in nums:
#     n  = insertIter(n, Node(el))


# print("max", findMaxIter(n))
# print("min", findMinIter(n))

# print("next 30", findNext(n, 30))
# print("prev 30", findPrev(n, 30))

print("delete 21")
n = deleteIter(n, 21)
print('---------------------------------------------------------\n\n\n---------------------------------------------------------')
print2D(n)

print("delete 30")
n = deleteIter(n, 30)
print('---------------------------------------------------------\n\n\n---------------------------------------------------------')
print2D(n)


# inOrder(n)
print()

