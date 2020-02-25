class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

"""
implement insert, delete, find next, find prev
find min and find max iteratively

sources used: https://www.geeksforgeeks.org/iterative-searching-binary-search-tree/
"""

class BinaryTreeRec:
    def __init__(self):
        self.root = Node(None)
    
    def insertIter(self, root, nd):
        if root == None: 
            root = nd
        else:
            while True:
                if nd.data <= root.data:
                    if root.left == None:
                        root.left = nd
                        root.left.parent = root
                        break
                    else:
                        root = root.left
                else:
                    if root.right == None:
                        root.right = nd
                        root.left.parent = root
                        break
                    else:
                        root = root.right

    def deleteIter(self, n):
        if n.left == None and n.right == None:
            n = None
        #


    def findMaxIter(self, root):
        while True:
            if root.right == None:
                return root.data
            else:
                root = root.right

    def findMinIter(self, root):
        while True:
            if root.left == None:
                return root.data
            else:
                root = root.left
    
    def findNext(self, root, num):
        #pseudocode
        """
        max = find max

        if num == max.data:
            return -1
        else:

        """