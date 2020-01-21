import networkx as nx 
import random
import matplotlib.pyplot as plt 
import operator

G = nx.gnp_random_graph(10, 0.5, directed = True) #(nodes,probability, direction)
nx.draw(G, with_labels=True)
plt.show()
#x random source node
x = random.choice([i for i in range(G.number_of_nodes())])
dict_counter = {}

for i in range(G.number_of_nodes()):
    dict_counter[i] = 0 

dict_counter[x] = dict_counter[x] + 1 

#iteration

for i in range(1000000000000):
    list_n = list(G.neighbors(x))
    if len(list_n) == 0:#If x is sink
        x = random.choice([i for i in range(G.number_of_nodes())])#choose random node
        dict_counter[x] += 1
    else:
        x = random.choice(list_n) #Select a neigbour
        dict_counter[x] += 1

p = nx.pagerank(G)
sorted_p = sorted(p.items(), key = operator.itemgetter(1))
sorted_rw = sorted(dict_counter.items(), key=operator.itemgetter(1))
print(sorted_p)
print(sorted_rw)
