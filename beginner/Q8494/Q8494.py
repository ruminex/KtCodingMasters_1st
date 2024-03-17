'''I = [int(x) for x in input().split()]

Lines = []

for a in range(0, I[1]):
    Lines.append(tuple(input()))'''

def print_graph(graph):
    for vertex, connections in graph.items():
        print(f"{vertex}: {' '.join(connections)}")


def build_graph():
    graph = {}
    while True:
        edge = input()
        if edge == "done":
            break
        v1, v2 = edge.split()

        if v1 not in graph:
            graph[v1] = [v2]
        else:
            graph[v1].append(v2)
        if v2 not in graph:
            graph[v2] = [v1]
        else:
            graph[v2].append(v1)
    return graph


graph = build_graph()


print()
print_graph(graph)