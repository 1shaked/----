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

def addElementWithLinarProbing(arr, index,element):
    while len(arr) < index + 1 or arr[index] is not None:
        if len(arr) < index:
            for i in range(index - len(arr) + 1):
                arr.append(None)
            break
        index = index + 1
    arr[index] = element
    return arr



keys :list = [12,9,33,54,27,38, 57, 83 , 16,32,22,60,72,50]
h1_obj: list = []
h2_obj:list = []

for key in keys:
    n = Node(key)
    index = h1(key)
    index_h2 = h2(key)
    addElementWithLinarProbing(h1_obj, index, n)
    addElementWithLinarProbing(h2_obj, index_h2, n)

    

print('H1 Here')
for i, v in enumerate(h1_obj):
    print(i, v)


print('H2 Here', '*' * 100)
for i, v in enumerate(h2_obj):
    print(i, v)

