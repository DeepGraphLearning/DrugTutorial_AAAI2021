import torch
from drugdiscovery import data

edge_list = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]
graph = data.Graph(edge_list, num_node=6)
graph.visualize("graph.png")

triplet_list = [[0, 1, 0], [1, 2, 1], [2, 3, 0], [3, 4, 1], [4, 5, 0], [5, 0, 1]]
graph = data.Graph(triplet_list, num_node=6, num_relation=2)
graph.visualize("relational_graph.png")

mol = data.Molecule.from_smiles("C1=CC=CC=C1")
mol.visualize("benzene.png")

graphs = [graph, graph, graph, graph]
batch = data.Graph.pack(graphs)
batch.visualize("batch.png", num_row=1)

g1 = graph.subgraph([1, 2, 3, 4])
g1.visualize("subgraph.png")

g2 = graph.node_mask([1, 2, 3, 4])
g2.visualize("node_mask.png")

g3 = graph.edge_mask([0, 1, 5])
g3.visualize("edge_mask.png")

g4 = g3.compact()
g4.visualize("compact.png")

graph_ids = torch.tensor([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
node_ids = torch.tensor([1, 2, 3, 4, 0, 1, 2, 3, 4, 5])
node_ids += batch.num_cum_nodes[graph_ids] - batch.num_nodes[graph_ids]
batch = batch.node_mask(node_ids)
batch.visualize("batch_node_mask.png", num_row=1)

batch = batch[[0, 1]]
batch.visualize("subbatch.png")