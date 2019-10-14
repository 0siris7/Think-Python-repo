import networkx as nx 
import matplotlib.pyplot as plt
G = nx.barbell_graph(4,22)


nx.draw(G)
plt.show()