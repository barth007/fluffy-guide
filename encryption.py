import math
import networkx as nx
import matplotlib.pyplot as plt

sender_secret = None
while sender_secret == None:
    sender_secret = int(input("enter your secret key (in form of integer): "))
    if isinstance(sender_secret, int):
        print("your key is being used...")
    else:
        sender_secret = None
print(sender_secret)

beta_values = []
gamma_values = []

def encryption(plain_text):
    # <-----------------------------------ENCRYPTION----------------------------------> 

    #storing ascii value of each character plain text character
    actual_ascii_values = []
    for letter in plain_text:
        val = ord(letter)
        actual_ascii_values.append(val)
    
    # shift cipher method which returns a cipher text after shift 'm%26' positions from original position
    def shift_cipher_encoder(ascii_values):
        s = sender_secret
        ciphertext = ""
        for value in ascii_values:
            shifted = (value - 65 + s) % 26 + 65
            
            ciphertext += chr(shifted)

        return ciphertext
    # returned encoded text from shift_cipher_encoder method
    encoded_text = shift_cipher_encoder(actual_ascii_values)

    #alpha values calculation according to the each character in encoded_text 
    alpha_values = []
    for char in encoded_text:
        alphaval = (ord(char) - 65) + 1
        alpha_values.append(alphaval)

    #beta values calculation
    for alpha_i in alpha_values:
        beta_i = 27  
        while math.gcd(beta_i, alpha_i) != 1 or beta_i in beta_values:
            beta_i += 1

        beta_values.append(beta_i)

    # gamma values calculation
    for i in range(len(alpha_values)):
        inv = pow(alpha_values[i],-1, beta_values[i])
        gamma_values.append(inv)

    print("<-------------FROM encryption.py file------------------------------------->")
    print("alpha values: ", alpha_values)
    print("beta values from encryption.py file: ", beta_values)
    print("gamma values from encryption.py file: ", gamma_values)
    print("<-------------------------------------------------------------------------->")

    # <<------------------------- Graph-------------------------------->>
    # Create the cycle graph C_n 
    cycle_graph = nx.cycle_graph(beta_values)
    
    # Create a new graph for the corona graph C_n⨀K_1
    corona_graph = nx.Graph()
    
    # Add nodes and edges from the cycle graph C_n
    corona_graph.add_nodes_from(cycle_graph)
    corona_graph.add_edges_from(cycle_graph.edges())
    
    # Add additional vertices for the K_1 component
    k1_vertices = [i for i in range(len(gamma_values))]
    for i in range(len(k1_vertices)):
        corona_graph.add_node(i, value=gamma_values[i])

    # Connecting pendant vertices with the inner vertices
    for ver, k_ver in zip(beta_values, k1_vertices):
        corona_graph.add_edge(ver, k_ver)

    # Print the gamma values associated with the K_1 component
    # print("Gamma Values of K_1 Component:")
    # for i in range(len(k1_vertices)):
    #     print("Value of vertex", i, ":", corona_graph.nodes[i]['value'])

    # Visualization
    pos = nx.spectral_layout(corona_graph)
    nx.draw(corona_graph, pos, with_labels=True)
    col_labels = ['vertex labels', 'values']

    table_vals = []
    for i in range(len(gamma_values)):
        table_vals.append([k1_vertices[i], gamma_values[i]])


    plt.table(cellText=table_vals,
            colWidths=[0.1] * 2,
            colLabels=col_labels,
            loc='upper right')

    plt.show()
    plt.axis('off')

    return {"beta_values": beta_values, "gamma_values": gamma_values}
