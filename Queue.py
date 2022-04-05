class Node:
    def __init__(self, data, nextV = None):
        self.v = data
        self.n = nextV
    
    def printNode(self):
        print(self.v);

class Queue:

    def __init__(self):
        # Fill here
        self.root = None

    def isEmpty(self):
        return self.root is None

    def print(self):
        root = self.root
        while root is not None:
            print(f'{root.v} -> ', end=' ')
            root = root.n

    def EnQueue(self, item):
        if (self.isEmpty):
            self.root = item
            return self.root
        root = self.root
        prev = None
        while root is not None:
            prev = root
            root = root.n

        prev.n = item

    def DeQueue(self):
        # [1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9]
        root = self.root
        nextV = root.n
        prev = None
        while nextV is not None:
            nextV = nextV.n
            prev = root
            root = root.n

        root.printNode()
        prev.n = None
     
    def top(self):
        return self.root
    def __str__(self):
        return f'root value is {self.root.v}'


if __name__ == '__main__':
    q = Queue()
    n3 = Node(10)
    q.EnQueue(n3)
    q.print()
    print(' - ')
    n2 = Node(9, n3)
    q.EnQueue(n2)
    n1 = Node(8, n2)
    q.EnQueue(n1)
    q.DeQueue()
    q.print()
    top = q.top()

    print(top)
