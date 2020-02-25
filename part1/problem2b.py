import random
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

def inOrder(n):
    if n:
        inOrder(n.right)
        print(n.data, end = " ")
        inOrder(n.left)

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

def inOrderArr(n, arr):
    if (n == None):
        return arr
    
    if (n.left):
        return inOrderArr(n.left, arr)
    arr.append(n.data)
    if (n.right):
        return inOrderArr(n.right, arr)

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

n = getRandomArray(12)
print(n)


tree = Node(1)
for num in n:
    insertRec(tree, Node(num))

m = []
# inOrderArr(tree, m)
# print()
inOrder(tree)
print(m)