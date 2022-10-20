from __future__ import annotations
import math
class Node:
    
    def __init__(self, number: int):
        self.number = number
        self.edges: list[Edge] = []

    def sortEdges(self):
        self.edges.sort(key=lambda x: x.w)

class Edge:
    w = math.inf # the weight of the edge
    is_added = False
    def __init__(self, start: Node, end: Node):
        self.start: Node = start
        self.end: Node = end
        
    
class Graph: 
    def __init__(self, vertices: list[Node]) :
        self.vertices = vertices
        # self.edges = edges

    def primeAlgorithm(self, s: Node) -> set[Edge]:
        tree_nodes: set[Node] = {s}
        # self.edges.sort(key=lambda e: e.w)
        while len(tree_nodes) != len(self.vertices):
            # min_edge = min(edges, key=lambda e: e.w)
            edge = self.getMinEdgeToAdd(tree_nodes)
            tree_nodes.add(edge.start)
            tree_nodes.add(edge.end)
            edge.is_added = True


        return self.getAddedEdges()

    def getAddedEdges(self) -> set[Edge]:
        edges: set[Edge] = set()
        for vertex in self.vertices:
            for edge in vertex.edges:
                if edge.is_added:
                    edges.add(edge)
        return edges
    def getMinEdgeToAdd(self, currentTree: set[Node]) -> Edge:
        current: Edge = None
        edges = self.getMinEdges(currentTree) # list of edges that are in the tree
        for edge in edges:
                
            is_start_not_in: bool = edge.start not in currentTree
            is_end_not_in  : bool = edge.end not in currentTree
            is_min_current = (current != None and current.w < edge.w)
            if  (is_start_not_in or is_end_not_in) and (is_min_current or current == None):
                # find the edge to add 
                current = edge
                break
            
            # elif start == len()

        if current == None:
            raise ValueError('the graph has internal error with is edges')

        return current       
        
    
    def edges(self):
        edges: list[list[Edge]] = [] # list of list with edges
        for vertex in self.vertices:
            edges[vertex.number - 1] = vertex.edges

    def getMinEdges(self, tree: set[Node])-> list[Edge]:
        edges: set[Edge] = set() # list of list with edges
        for vertex in tree:
            for edge in vertex.edges:
                if not edge.is_added:
                    edges.add(edge)
        edges_list: list[Edge] = list(edges)
        edges_list.sort(key=lambda e: e.w) # list of list with edges
        return edges_list
        


nodes = [Node(x) for x in range(1,5)]

n1_to_2 = Edge(nodes[0], nodes[1])
n1_to_2.w = 2

n1_to_3 = Edge(nodes[0], nodes[2])
n1_to_3.w = 1

n1_to_4 = Edge(nodes[0], nodes[3])
n1_to_4.w = 4

n2_to_3 = Edge(nodes[1], nodes[2])
n2_to_3.w = 1

n2_to_4 = Edge(nodes[1], nodes[3])
n2_to_4.w = 3

n3_to_4 = Edge(nodes[2], nodes[3])
n3_to_4.w = 5

edges: list[Edge] = [
    n1_to_2, n1_to_3, n1_to_4, n2_to_3, n2_to_4, n3_to_4
]

nodes[0].edges = [n1_to_2, n1_to_3, n1_to_4]
nodes[1].edges = [n1_to_2, n2_to_3, n2_to_4]
nodes[2].edges = [n3_to_4, n2_to_3, n1_to_3]
nodes[3].edges = [n3_to_4, n2_to_4, n1_to_4]


for node in nodes:
    node.sortEdges()


G = Graph(nodes)
tree: set[edges] = G.primeAlgorithm(nodes[0])

print(tree)

for edge in tree:
    print(f'{edge.start.number} <---> {edge.end.number}')