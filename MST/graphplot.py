import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
edgelist=[]

def addEdge(edge_list):
    for i in edge_list:
        G.add_edge(i[0],i[1],len=i[2])


def createEdgelist(edge_list):
    for i in edge_list:
        edgelist.append((i[0],i[1]))

def drawGraph(node_list, edge_list):
    addEdge(edge_list)
    createEdgelist(edge_list)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_edges(G, pos,edgelist=edgelist, width=4)
    nx.draw_networkx_labels(G, pos, font_size=15, font_family="sans-serif")
    nx.draw_networkx_edge_labels(G, pos, font_size=10, font_family="sans-serif")
    # nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
