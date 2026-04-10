import re


def get_path(dest, predecessors):
    path = []
    path.insert(0, dest)

    if dest in predecessors:
        pred = predecessors[dest]
    else:
        return path

    while pred is not None:
        path.insert(0, pred)
        if pred in predecessors:
            pred = predecessors[pred]
        else:
            pred = None
    return path


def next_nearest_node(distances, unvisited):
    pass


def main():
    dest = "York"
    # predecessors = {"York": "London", "Hampshire": "Manchester", "London": "Hampshire"}
    predecessors = {}
    path = get_path(dest, predecessors)
    print(path)


if __name__ == "__main__":
    main()
