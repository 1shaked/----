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

keys :list = [16,12,9,33,54,27,69,38, 57, 83 , 16,32,22,60,72,50]
h1_obj: list = []
h2_obj:list = []

for key in keys:
    n = Node(key)
    index = h1(key)
    h1_len = len(h1_obj)
    if  h1_len < index + 1:
        for i in range(index - h1_len+ 1):
            h1_obj.append(None)
    if h1_obj[index] is not None:
        h1_obj[index].nextV = n
    else:
        h1_obj[index] = n 

    index_h2 = h2(key)
    h2_len = len(h2_obj)
    if  h2_len < index_h2 + 1:
        for i in range(index_h2 - h2_len + 1):
            h2_obj.append(None)
    if h2_obj[index_h2] is not None:
        h2_obj[index_h2].nextV = n
    else:
        h2_obj[index_h2] = n

print('H1 Here')
for i, v in enumerate(h1_obj):
    print(i, v)


print('H2 Here', '*' * 100)
for i, v in enumerate(h2_obj):
    print(i, v)

