from __future__ import annotations
import math
class Node:
    
    def __init__(self, number: int):
        self.number = number
        self.edges: list[Edge] = []
        self.paths: int = 0
        self.distance: int = math.inf
        self.origin: Node = self
        self.marked: bool = False

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

    def BfsCountWays(self, s: Node):
        queue: list[Node] = [s]
        s.distance = 0
        s.paths = 1
        while len(queue) > 0:
            node: Node = queue.pop(0)
            nodes: set[Node] = self.getNodesFromEdges(node.edges)
            if node in nodes:
                nodes.remove(node)
            if node.marked:
                continue
            for vertex in nodes:
                is_inf_distance: bool = vertex.distance == math.inf
                is_distance_improvement: bool = node.distance + 1 == vertex.distance
                if (not is_inf_distance and is_distance_improvement) or (is_inf_distance):
                    vertex.origin = node
                    vertex.paths += node.paths
                    vertex.distance = node.distance + 1
                    queue.append(vertex)
                if node.distance + 1 < vertex.distance:
                    raise ValueError("Distance must be greater less then that value.")
                    
                    
            node.marked = True
            if s != node:
                print(f'paths ->{node.paths} at node {node.number}, with distance {node.distance}')
        s.paths = 0
        print(f'paths ->{s.paths} at node {s.number}, with distance {s.distance}')



    def getNodesFromEdges(self, edges: list[Edge]) -> set[Node]:
        s: set[Node] = set()
        for edge in edges:
            s.add(edge.start)
            s.add(edge.end)

        return s




nodes = [Node(x) for x in range(0,6)]

n0_to_1 = Edge(nodes[0], nodes[1])
n0_to_1.w = 2

n0_to_5 = Edge(nodes[0], nodes[5])
n0_to_5.w = 1

n1_to_2 = Edge(nodes[1], nodes[2])
n1_to_2.w = 4

n2_to_3 = Edge(nodes[2], nodes[3])
n2_to_3.w = 1

n2_to_4 = Edge(nodes[2], nodes[4])
n2_to_4.w = 3

n5_to_2 = Edge(nodes[5], nodes[2])
n5_to_2.w = 5


n5_to_3 = Edge(nodes[5], nodes[3])
n5_to_3.w = 3

nodes[0].edges = [n0_to_1, n0_to_5] # node 0
nodes[1].edges = [n1_to_2]
nodes[2].edges = [n2_to_3, n2_to_4]
nodes[5].edges = [n5_to_2, n5_to_3]


G = Graph(nodes)
G.BfsCountWays(nodes[0])

