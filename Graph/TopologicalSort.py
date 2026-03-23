from collections import defaultdict


class Graph:
    # Time complexity - O(v+E) and O(v+E)
    def __init__(self , numberVertices):
        self.graph = defaultdict(list)
        self.numberVertices = numberVertices
    
    def add_edge(self , vertex , edge):
        self.graph[vertex].append(edge)
    
    def topologicalUtil(self,v,visited,stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topologicalUtil(i,visited,stack)
        
        stack.insert(0,v)
    
    def topologicalSort(self):
        visited = []
        stack = []
        for k in list(self.graph):
            if k not in visited:
                self.topologicalUtil(k,visited,stack)
        
        print(stack)

graph = Graph(8)
graph.add_edge("A","C")
graph.add_edge("B","C")
graph.add_edge("C","E")
graph.add_edge("E","H")
graph.add_edge("E","F")
graph.add_edge("F","G")
graph.add_edge("B","D")
graph.add_edge("D","F")

graph.topologicalSort()