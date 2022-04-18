class Node():
    def __init__(self, v):
        self.v = v
        self.nextV = None
    def __str__(self):
        return f'{self.v} n => {self.nextV}'
m = 19
def h1(k):
    return k % m
def h2(k):
    return ( k % (m-1) ) + 1

def addElementWitDoubleHashing(arr, index,element, fn):
    i = 0
    currentIndex = index
    while len(arr) < currentIndex + 1 or arr[currentIndex] is not None:
        if len(arr) < currentIndex:
            for _ in range(currentIndex - len(arr) + 1):
                arr.append(None)
            break
    
        i += 1
        currentIndex = index + i * fn(element.v)
        
    arr[currentIndex] = element
    return arr



keys :list = [12,9,33,54,27,69,38, 57, 83 , 16,32,22,60,72,50]
h1_obj: list = []
h2_obj:list = []

for key in keys:
    n = Node(key)
    index = h1(key)
    addElementWitDoubleHashing(h1_obj, index, n, h2)

    

print('H1 Here')
for i, v in enumerate(h1_obj):
    print(i, v)


