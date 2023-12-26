import networkx as nx
f = open('input.txt', 'r')
lines = f.read().split('\n')

components = {}
for line in lines:
    colonIndex = line.index(':')
    name, connections = line[0:colonIndex], line[colonIndex+2:].split(' ')
    components[name] = connections

graph = nx.Graph()
for componentName, connections in components.items():
    for name in connections:
        graph.add_edge(componentName, name)
cuts = nx.minimum_edge_cut(graph)
graph.remove_edges_from(cuts)

groups = list(nx.connected_components(graph))

print(len(groups[0])*len(groups[1]))