import re


# Create an empty unvisited set to keep track of the nodes that haven't yet been visited.
# Create an empty predecessors dictionary to keep track of the path we're traversing.
# Create an empty distances dictionary to keep track of the shortest known distance from src to each node.
# Add each node to the unvisited set.
# Set the distance to the src node to 0.
# Set the distances to all other nodes to positive infinity.
# While there are still nodes to visit:
# Get the unvisited node with the minimum distance from src using next_nearest_node.
# Mark that node as visited.
# If this next_nearest is the destination:
# We're done! Return the path to dest using get_path.
# Otherwise:
# For each unvisited neighbor of next_nearest:
# Get the currently known distance to next_nearest.
# Get the distance in the graph between next_nearest and the neighbor.
# Combine those 2 values to calculate the total distance from src to the neighbor.
# If the total distance to the neighbor is less than the distance we previously had stored for the neighbor in the distances dictionary:
# Update the distance we have stored for the neighbor.
# Update the predecessor of the neighbor to be next_nearest.
def dijkstra(graph, src, dest):
    unvisited = set()
    predecessors = {}
    distances = {}
    for node in graph:
        unvisited.add(node)
        distances[node] = float("inf")
    distances[src] = 0

    while len(unvisited) > 0:
        next_nearest = next_nearest_node(distances, unvisited)
        unvisited.remove(next_nearest)

        if next_nearest == dest:
            return get_path(dest, predecessors)

        for neighbour in graph[next_nearest]:
            if neighbour not in unvisited:
                continue

            dist_so_far = distances[next_nearest]
            dist_to_neighbour = graph[next_nearest][neighbour]
            total_dist_to_neighbour = dist_so_far + dist_to_neighbour

            if total_dist_to_neighbour < distances[neighbour]:
                distances[neighbour] = total_dist_to_neighbour
                predecessors[neighbour] = next_nearest


# This function returns a list of nodes representing
# the path that was taken through the graph by following the predecessors.
# Starting at the dest node, traverse the predecessors
# dictionary backwards, building the final path as you go.
def get_path(dest, predecessors):
    path = []
    pred = dest

    while pred is not None:
        path.append(pred)
        pred = predecessors.get(pred, None)
    path.reverse()

    return path


# returns the closest unvisited node.
def next_nearest_node(distances, unvisited):
    min_dist = float("inf")
    next_nearest = None

    for v in unvisited:
        distance_so_far = distances[v]
        if distance_so_far < min_dist:
            min_dist = distance_so_far
            next_nearest = v
    return next_nearest


def main():

    graph = {
        "Minas Tirith": {"Isengard": 4, "Gondor": 1},
        "Isengard": {"Minas Tirith": 4, "Bree": 3, "Mirkwood": 8},
        "Gondor": {"Minas Tirith": 1, "Bree": 2, "Misty Mountains": 6},
        "Bree": {"Gondor": 2, "Isengard": 3, "Mirkwood": 4},
        "Mirkwood": {"Bree": 4, "Isengard": 8, "Lothlorien": 2},
        "Misty Mountains": {"Gondor": 6, "Lothlorien": 8},
        "Lothlorien": {"Misty Mountains": 8, "Mirkwood": 2},
    }
    src = "Isengard"
    dest = "Gondor"
    # expect:["Isengard", "Bree", "Gondor"],
    path = dijkstra(graph, src, dest)
    print(path)


if __name__ == "__main__":
    main()
