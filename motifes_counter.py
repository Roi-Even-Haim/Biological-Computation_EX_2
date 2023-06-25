from itertools import combinations
import networkx as nx
import sys

n = int(input("Enter a positive integer: "))
if(n==1):
    sys.exit("invalid input (n=1)")

G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (1,4)])

all_edges = list(G.edges())

# Initialize a list to store the subgraphs
subgraphs = []
combination = []

# Generate all possible combinations of edges of size n-1
for length in range(1,len(all_edges)+1):

    for comb in combinations(all_edges, length):
        combination.append(list(comb))
        

    
#print(combination)
# Iterate over each combination
for combo in combination:
    # Create a new subgraph  
    subgraph = nx.DiGraph()
  
    # Add the selected edges to the subgraph
    subgraph.add_edges_from(combo)

    # Check if the subgraph is connected and in size n
    if  subgraph.number_of_nodes() == n:
        subgraphs.append(subgraph)
    

# Check isomorphism between the sub-graphs
motifes = {subgraphs[0]:[]}
for g in subgraphs:

    isunqiue = False    
    for unique in motifes.keys():
        if nx.is_isomorphic(g,unique):
            motifes[unique].append(g)
            isunqiue = True
            break
    if not isunqiue:
        motifes[g] = [g]




if (n == 1):
    with open("sub-graphs_motifes.txt","wt") as f:
        f.write("no edges")
else:
    with open("sub-graphs_motifes.txt","wt") as f:
        f.write("n="+str(n)+"\n")
        f.write("count num of sub-graphs="+str(len(subgraphs))+"\n")
        for i, motif in enumerate(motifes):
            f.write("#" + str(i+1) + "\n")
            f.write("count="+str(len(motifes[motif]))+"\n")
            for edge in motifes[motif][0].edges():
                f.write(str(edge[0]) + " " + str(edge[1]) + "\n")

