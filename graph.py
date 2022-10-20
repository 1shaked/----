
from __future__ import annotations

class Node:
    def __init__(self,v: int, parent: Node= None):
        self.parent: Node = parent
        self.v: int = v
        self.rank: int = 0

    def FindSetRec(self) -> Node:
        if self.parent == None:
            return self
        return self.parent.FindSetRec(self.parent)
        
    def FindSetWithFixTimeForRec(self) -> Node:
        if self.parent == None:
            return self

        parent = self.FindSetRec(self)
        self.parent = parent
        return parent

    def FindSetIter(self) -> Node:
        if self.parent == None:
            return self
        current = self
        base = self
        while current.parent != None:
            current = current.parent
        base.parent = current
        return current
    def IncrementRank(self) -> None:
        self.rank += 1

def Link(n1: Node, n2: Node)  -> None:
    if n1.rank > n2.rank:
        n2.parent = n1
    else:
        n1.parent = n2
        if n1.rank == n2.rank:
            n2.IncrementRank()
    


nodes: list[Node] = [Node(x, None) for x in range(5)] # vertex

edges: list[list[int]] = [
    [0,1],
    [2,3],
    [1,2],
    [0,4],
    [4,3]
]

# this will detect cycles in the undirected graph
for edge in edges:
    start, end = edge[0], edge[1]
    startNode: Node = nodes[start]
    endNode: Node = nodes[end]
    if startNode.FindSetIter() == endNode.FindSetIter():
        Link(startNode, endNode)
        print('cycle')
        break
    elif startNode.parent == None:
        startNode.parent = endNode
        endNode.IncrementRank()
        continue
    
    elif endNode.parent == None:
        endNode.parent = startNode.parent
        startNode.IncrementRank()
        continue
    

