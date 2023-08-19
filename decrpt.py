from decryption import decryption
import matplotlib.pyplot as plt
import networkx as nx

l1 = input("beta: ")
l2 = input("gamma: ")

bv = []
temp_num = ""
for i in l1.strip(' ' + '\n' + ''):
    if str(i).isdigit():
        temp_num += str(i)
    elif str(i) == ',' or str(i) == ']':
        bv.append(int(temp_num))
        temp_num = ""

gv = []
temp_num = ""
for i in l2.strip(' ' + '\n' + ''):
    if str(i).isdigit():
        temp_num += str(i)
    elif str(i) == ',' or str(i) == ']':
        gv.append(int(temp_num))
        temp_num = ""

# # Create the cycle graph C_n 
# cycle_graph = nx.cycle_graph(bv)

# # Create a new graph for the corona graph C_n⨀K_1
# corona_graph = nx.Graph()

# # Add nodes and edges from the cycle graph C_n
# corona_graph.add_nodes_from(cycle_graph)
# corona_graph.add_edges_from(cycle_graph.edges())

# # Add additional vertices for the K_1 component
# k1_vertices = [i for i in range(len(gv))]
# for i in range(len(k1_vertices)):
#     corona_graph.add_node(i, value=gv[i])

# # Connecting pendant vertices with the inner vertices
# for ver, k_ver in zip(bv, k1_vertices):
#     corona_graph.add_edge(ver, k_ver)

# # Print the gamma values associated with the K_1 component
# print("Gamma Values of K_1 Component:")
# for i in range(len(k1_vertices)):
#     print("Value of vertex", i, ":", corona_graph.nodes[i]['value'])

decryption(bv, gv)
