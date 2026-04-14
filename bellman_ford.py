def bellman_ford(graph, src, dest):
    distances = {}
    for node in graph:
        distances[node] = float("inf")
    distances[src] = 0

    for _ in range(len(graph) - 1):
        for node1 in graph:
            for node2 in graph[node1]:
                weight = graph[node1][node2]
                relax_edge(distances, node1, node2, weight)

    for node1 in graph:
        for node2 in graph[node1]:
            weight = graph[node1][node2]
            is_neg_cycle = relax_edge(distances, node1, node2, weight)
            if is_neg_cycle:
                raise Exception("negative cycle detected!")
    return distances[dest]


# Don't touch below this line


def relax_edge(distances, node1, node2, weight_1_2):
    if distances[node1] + weight_1_2 < distances[node2]:
        distances[node2] = distances[node1] + weight_1_2
        return True

    return False
