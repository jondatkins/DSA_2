import random


def heuristic(next, dest):
    dist = abs(next.x - dest.x) + abs(next.y - dest.y)
    return dist


def a_star_search(traffic_grid, src, dest):
    queue = PriorityQueue()
    queue.push(0, src)
    predecessors = {}
    predecessors[src] = None
    lowest_costs = {}
    lowest_costs[src] = 0
    visited = set()
    while not queue.empty():
        tile = queue.pop()
        if tile == dest:
            break
        if tile in visited:
            continue
        else:
            visited.add(tile)
        for neighbor in traffic_grid.neighbors(tile):
            total_cost = lowest_costs[tile] + neighbor.cost()
            if neighbor not in lowest_costs or total_cost < lowest_costs[neighbor]:
                lowest_costs[neighbor] = total_cost
                neighbor_priority = heuristic(neighbor, dest)
                neighbor_priority = neighbor_priority + total_cost
                queue.push(neighbor_priority, neighbor)
                predecessors[neighbor] = tile
    path = []
    pred = dest
    while pred is not None:
        path.append(pred)
        pred = predecessors[pred]

    path.reverse()
    return path


# Don't touch below this line


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def push(self, priority, item):
        self.elements.append((priority, item))

    def pop(self):
        if self.empty():
            return None
        min = 0
        for i in range(len(self.elements)):
            if self.elements[i][0] < self.elements[min][0]:
                min = i
        item = self.elements[min]
        del self.elements[min]
        return item[1]


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cost(self):
        random.seed(hash(self))
        bucket = random.randint(1, 2)
        cost = random.randint(1, 5)
        if bucket == 2:
            cost = random.randint(15, 20)
        return cost

    def __eq__(self, other):
        if other is None:
            return False
        if type(other) is tuple:
            return self.x == other[0] and self.y == other[1]
        else:
            return self.x == other.x and self.y == other.y

    def __hash__(self):
        return (self.x * 1000) + self.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class TrafficGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def in_bounds(self, tile):
        return 0 <= tile.x < self.width and 0 <= tile.y < self.height

    def neighbors(self, tile):
        neighbors = [
            Tile(tile.x + 1, tile.y),
            Tile(tile.x - 1, tile.y),
            Tile(tile.x, tile.y - 1),
            Tile(tile.x, tile.y + 1),
        ]
        results = filter(self.in_bounds, neighbors)
        return results

    def __repr__(self):
        s = ""
        for y in range(self.height - 1, -1, -1):
            for x in range(self.width):
                t = Tile(x, y)
                s += f"[{t.cost():02d}]"
            s += "\n"
        return s
