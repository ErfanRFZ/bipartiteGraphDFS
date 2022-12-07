from collections import defaultdict


class Graph:

    # Constructor (with +v variable)
    def __int__(self, v):
        self.V = v

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # function to check if graph is bipartite or not
    def isBipartite(self, v, visited, color):

        # loop through each node
        for u in self.graph.get(str(v)):

            # make u int
            u = int(u)
            # If vertex u is not explored before
            if not visited[u]:

                # Mark present vertices as visited
                visited[u] = True

                # Mark its color opposite to its parent
                color[u] = not color[v]

                # If the subtree rooted at vertex v
                # is not bipartite
                if not self.isBipartite(u, visited, color):
                    return False

            # If at any point, color[u] is equal to color[v], then the node is not bipartite.
            elif color[u] == color[v]:
                return False

        return True
