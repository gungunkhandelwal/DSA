# Simple Implementation

# class Graph:
#     def __init__(self,gdict=None):
#         if gdict is None:
#             gdict ={}
#         self.gdict = gdict
    
#     def addVertex(self,vertex,edges):
#         self.gdict[vertex].append(edges)

# customDict={
#     "a":["b","c"],
#     "b":["c","d","e"],
#     "c":["a","b","e"],
#     "e":["b","c"]
# }

# g = Graph(customDict)
# g.addVertex("a","e")
# print(g.gdict)

# Dynamic Implementation

from collections import deque

class Graph:
    def __init__(self):
        self.adjancey_list = {}
    
    def add_vertex(self , vertex):
        if vertex not in self.adjancey_list:
            self.adjancey_list[vertex]=[]
            return True
        return False
    
    def print_grapf(self):
        for vertex in self.adjancey_list:
            print(vertex,":",self.adjancey_list[vertex])

    def add_edge(self,vertex1 , vertex2):
        if vertex1 in self.adjancey_list.keys() and vertex2 in self.adjancey_list.keys():
            self.adjancey_list[vertex1].append(vertex2)
            self.adjancey_list[vertex2].append(vertex1)
            return True
        return False
    
    def remove_edge(self,vertex1,vertex2):
        try:
            if vertex1 in self.adjancey_list.keys() and vertex2 in self.adjancey_list.keys():
                self.adjancey_list[vertex1].remove(vertex2)
                self.adjancey_list[vertex2].remove(vertex1)
                return True
        except ValueError:
            pass
        return False
    
    def remove_vertex(self,vertex):
        if vertex in self.adjancey_list.keys():
            for other_vertex in self.adjancey_list[vertex]:
                self.adjancey_list[other_vertex].remove(vertex)
            del self.adjancey_list[vertex]
            return True
        return False
    

    # BFS
    def bfs(self,vertex):
        visited = set()
        visited.add(vertex)
        # queue = [vertex] -- due to time complexity of O(v^2+e)
        queue = deque([vertex])
        while queue:
            current_vertex = queue.popleft()
            print(current_vertex)
            for adjancet_vertex in self.adjancey_list[current_vertex]:
                if adjancet_vertex not in visited:
                    visited.add(adjancet_vertex)
                    queue.append(adjancet_vertex)
      
      
    def dfs(self , vertex):
        # visited = set()
        visited = set([vertex])
        stack = [vertex]
        while stack:
            current_vertex = stack.pop()
            print(current_vertex)
            # if current_vertex not in visited: --due to space complexity of O(v+e)
            #     print(current_vertex)
            #     visited.add(current_vertex)
            for adjancey_vertex in self.adjancey_list[current_vertex]:
                if adjancey_vertex not in visited:
                    # stack.append(adjancey_vertex)
                    visited.add(adjancey_vertex)
                    stack.append(adjancey_vertex)



    
graph = Graph()
# graph.add_vertex("A")
# graph.add_vertex("B")
# graph.add_vertex("C")
# graph.add_vertex("D")

# graph.add_edge('A','B')
# graph.add_edge('B','C')
# graph.add_edge('A','C')
# graph.add_edge('C','D')
# graph.add_edge('A','D')

# graph.print_grapf()

# print("Grapgh after removing")
# # graph.remove_edge('A','C')
# # graph.remove_edge("A","D")
# graph.remove_vertex('D')
# graph.print_grapf()


# New Graph
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')

# Adding edges
graph.add_edge('A','B')
graph.add_edge('A','C')
graph.add_edge('B','E')
graph.add_edge('C','D')
graph.add_edge('D','E')

# Print graph
graph.print_grapf()

# bfs
graph.bfs('A')
print()
print("THE DFS OF THE GRAPH")
print()
graph.dfs("A")
