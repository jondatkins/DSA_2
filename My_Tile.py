import random


class Tile:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def cost(self):
        seed = self.__hash__()
        random.seed(seed)
        return random.randint(1, 25)

    # Don't touch below this line

    def __hash__(self):
        return (self.x * 1000) + self.y

    def __repr__(self):
        return f"({self.x}, {self.y})"
