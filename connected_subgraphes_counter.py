from itertools import combinations
import networkx as nx
import time
start_time = time.time()




def generate_connected_subgraphs(n):
    # Create an empty graph
    graph = nx.complete_graph(n, nx.DiGraph())

    # Add nodes to the graph
    #graph.add_nodes_from(range(1, n+1))

    # Generate all possible edges
    all_edges = list(graph.edges())
    
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
        if nx.is_weakly_connected(subgraph) and subgraph.number_of_nodes() == n:
            subgraphs.append(subgraph)


    # Check isomorphism between the sub-graphs
    unique_graphs = [subgraphs[0]]
    for g in subgraphs:
        isIsomorphic = False
        for unique in unique_graphs:
            if nx.is_isomorphic(g,unique):
                isIsomorphic = True
                break
        
        if not isIsomorphic:    
            unique_graphs.append(g)

    return unique_graphs




#n = int(input("Enter a positive integer: "))

for n in range(1,8):
    if (n == 1):
        with open("connected_sub-graphs.txt","wt") as f:
            f.write("no edges")
    else:
        subgraphs = generate_connected_subgraphs(n)
        with open("connected_sub-graphs.txt","wt") as f:
            f.write("n="+str(n)+"\n")
            f.write("count="+str(len(subgraphs))+"\n")
            for i, subgraph in enumerate(subgraphs):
                f.write("#" + str(i+1) + "\n")
                for edge in subgraph.edges():
                    f.write(str(edge[0]+1) + " " + str(edge[1]+1) + "\n")
    print("n="+str(n)+"--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    






        
    







