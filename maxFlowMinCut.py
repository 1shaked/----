# Complexity : (E*(V^3))
# Total augmenting path = VE and BFS
# with adj matrix takes :V^2 times
 
# from collections import defaultdict
 
# This class represents a directed graph
# using adjacency matrix representation
class Graph:
 
    def __init__(self,graph):
        self.graph = graph # residual graph
        self.org_graph = [i[:] for i in graph]
        self.ROW = len(graph)
        self.COL = len(graph[0])
 
 
    '''Returns true if there is a path from
    source 's' to sink 't' in
    residual graph. Also fills
    parent[] to store the path '''
    def BFS(self,s, t, parent):
 
        # Mark all the vertices as not visited
        visited =[False]*(self.ROW)
 
        # Create a queue for BFS
        queue=[]
 
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        # Standard BFS Loop
        while queue:
 
            #Dequeue a vertex from queue and print it
            u = queue.pop(0)
 
            # Get all adjacent vertices of
            # the dequeued vertex u
            # If a adjacent has not been
            # visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0 :
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
            # if the sink has been visited there is a path that we already explored
            if visited[t]:
                return True
        # If we reached sink in BFS starting
        # from source, then return
        # true, else false
        return visited[t]
         
    # Function for Depth first search
    # Traversal of the graph
    def dfs(self, graph,s,visited):
        visited[s]=True
        for i in range(len(graph)):
            if graph[s][i]>0 and not visited[i]:
                self.dfs(graph,i,visited)
 
    # Returns the min-cut of the given graph
    def minCut(self, source: int, sink: int) -> list[list[int]]:
 
        # This array is filled by BFS and to store path
        parent = [-1]*(self.ROW)
 
        max_flow = 0 # There is no flow initially
 
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :
 
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            # Add path flow to overall flow
            max_flow += path_flow
 
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        visited=len(self.graph)*[False]
        # this get us the paths that have a zero weight and used to have positive number
        self.dfs(self.graph,s,visited)
 
        # print the edges which initially had weights
        # but now have 0 weight
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.graph[i][j] == 0 and\
                self.org_graph[i][j] > 0 and visited[i]:
                    print(str(i) + " - " + str(j))

        return max_flow
 
 
# Create a graph given in the above diagram
graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]


graph = [
#    0  ,1 , 2 , 3
    [0 , 2 , 2 , 0], # 0
    [0 , 0 , 0 , 1], # 1
    [0 , 0 , 0 , 1], # 2
    [0 , 0 , 0 , 0]  # 3
]
 
g = Graph(graph)
 
source = 0; sink = 5
source, sink = 0 , 3

 
g.minCut(source, sink)

 