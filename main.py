# AI Project
# @author: Erfan Rafezi

import os
import networkx as nx
from Graph import Graph
import matplotlib.pyplot as plt


# test func for checking the graph is Bipartite or not (networkx library)
def isBipartite(graph):
    # convert the listed graph to graph object of networkx library
    g = nx.Graph(graph)

    # Checking the graph for directed
    if g.is_directed():
        print("Graph is directed")

        # draw graph
        nx.draw(graph, pos=nx.spring_layout(graph), with_labels=1)
    else:
        print("Graph is not directed")

    # Checking Bipartite
    if nx.is_bipartite(g):
        print("Graph is bipartite")
    else:
        print("Graph is not bipartite")


# main function
def main():
    # Get all file name of graph (files format: edgelist)
    graphs = os.listdir('graph')

    # Test Bipartite with networkx library
    # test_bipartite(graphs)

    # Read all files in folder
    # list_graph = list(nx.edges(nx.read_edgelist("graph/graph3.edgelist")))

    # loop through files(names) in the folder
    # loop for check all graphs
    for fileName in graphs:
        print(f"\nChecking graph: '{fileName}'")

        # Read all edgelist with networkx library
        graph = list(nx.edges(nx.read_edgelist(f"graph/{fileName}")))

        # To get length of graph list
        i = len(graph)

        # To maintain the adjacency list of graph
        adj = [[] for i in range(len(graph))]

        # To check node visited or not
        visited = [0 for i in range(len(graph))]

        # To color the vertices (stores 0 or 1 for every node)
        color = [0 for i in range(len(graph))]

        g = Graph()
        for node in graph:
            # print(f"\n {node}= {node[0]}, {node[1]}")
            g.addEdge(node[0], node[1])

        # Marking the source node as visited
        # Start position
        visited[1] = True

        # Marking the source node with a color
        color[1] = 0

        # Check if the graph is Bipartite
        if g.isBipartite(1, visited, color):
            print("Graph is Bipartite")
            # print(f"nodes: {g.graph}")
        else:
            print("Graph is not Bipartite")

        # Get position of graph
        pos = nx.spring_layout(nx.Graph(graph))

        # Draw the graph
        nx.draw(nx.Graph(graph), pos=pos, with_labels=True)
        plt.show()


def test_bipartite(graphs):
    # loop for all file to check
    for fileName in graphs:
        print(f"\nChecking graph: '{fileName}'")

        # Read all edgelist with networkx library
        graph = list(nx.edges(nx.read_edgelist(f"graph/{fileName}")))
        isBipartite(graph)

        # Convert list to graph(graph object)
        g = nx.Graph(graph)
        graph1 = list(g.nodes)

        print(f"nodes: {sorted(graph1)}")


# main
if __name__ == '__main__':
    main()
