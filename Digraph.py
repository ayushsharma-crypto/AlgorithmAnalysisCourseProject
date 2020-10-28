import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

def addNodes(node_list):
    G.add_nodes_from(node_list)


def addEdge(edge_list):
    G.add_edges_from(edge_list)


def drawGraph(node_list, edge_list):
    addNodes(node_list)
    addEdge(edge_list)
    plt.figure(figsize =(20,20)) 
    nx.draw_networkx(G, with_labels = True, node_size=3000 ) 
    plt.show()

def get_all_indegree():
    return G.in_degree()