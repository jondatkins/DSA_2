class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        if len(self.elements) == 0:
            return True
        return False

    def push(self, priority, item):
        self.elements.append((priority, item))

    def pop(self):
        if len(self.elements) == 0:
            return None
        min_index_so_far = 0
        for i in range(len(self.elements)):
            if self.elements[i][0] < self.elements[min_index_so_far][0]:
                min_index_so_far = i
        min_tup = self.elements[min_index_so_far][1]
        del self.elements[min_index_so_far]
        return min_tup


def main():
    pass


if __name__ == "__main__":
    main()
