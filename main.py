import re


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


def next_nearest_node(distances, unvisited):
    smallest = -1
    nearest = ""
    for idx, node in enumerate(unvisited):
        if node in distances:
            if idx == 0:
                smallest = distances[node]
                nearest = node
            elif distances[node] < smallest:
                smallest = distances[node]
                nearest = node
    if smallest == -1:
        return None
    return nearest


def main():
    distances = {"Hartford": 7, "New Haven": 2, "Greenwich": 3}
    unvisited = {"Hartford", "Greenwich"}
    next_nearest = next_nearest_node(distances, unvisited)
    print(next_nearest)


if __name__ == "__main__":
    main()
