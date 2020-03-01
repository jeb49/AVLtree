import random

#a
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
print(getRandomArray(12))

#b

def getSortedArray(n):
    arr = []
    for i in range(n):
        num = n - i
        arr.append(num)
    return arr
print(getSortedArray(12))

        