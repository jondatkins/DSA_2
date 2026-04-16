class MinHeap:
    def pop(self):
        if len(self.elements) == 0:
            return None
        if len(self.elements) == 1:
            elem = self.elements[0]
            del self.elements[0]
            return elem
        root_elem = self.elements[0]
        last_elem = self.elements.pop()
        self.elements[0] = last_elem
        self.bubble_down(0)
        return root_elem

    def bubble_down(self, index):
        left_child_indx = 2 * index + 1
        right_child_indx = 2 * index + 2
        # left_child = self.elements[left_child_indx]
        # right_child = self.elements[right_child_indx]
        heap_len = len(self.elements)
        if left_child_indx >= heap_len and right_child_indx >= heap_len:
            return
        smallest_child_indx = -1
        if left_child_indx <= heap_len and right_child_indx >= heap_len:
            smallest_child_indx = left_child_indx
        elif left_child_indx >= heap_len and right_child_indx <= heap_len:
            smallest_child_indx = right_child_indx
        elif left_child_indx <= heap_len and right_child_indx <= heap_len:
            if self.elements[left_child_indx][0] < self.elements[right_child_indx][0]:
                smallest_child_indx = left_child_indx
            else:
                smallest_child_indx = right_child_indx
        if smallest_child_indx != -1:
            if self.elements[smallest_child_indx][0] < self.elements[index][0]:
                child_elem = self.elements[smallest_child_indx]
                self.elements[smallest_child_indx] = self.elements[index]
                self.elements[index] = child_elem
                self.bubble_down(smallest_child_indx)

    # Don't touch below this line

    def push(self, priority, value):
        self.elements.append((priority, value))
        self.bubble_up(len(self.elements) - 1)

    def bubble_up(self, index):
        if index == 0:
            return

        parent_index = (index - 1) // 2
        parent_priority = self.elements[parent_index][0]
        current_priority = self.elements[index][0]

        if parent_priority > current_priority:
            self.elements[parent_index], self.elements[index] = (
                self.elements[index],
                self.elements[parent_index],
            )
            self.bubble_up(parent_index)

    def __init__(self):
        self.elements = []

    def peek(self):
        if len(self.elements) == 0:
            return None

        return self.elements[0][1]


def main():
    min_heap = MinHeap()
    push_inputs = [
        (5, "Street of Steel"),
        (3, "Kingsroad"),
        (7, "Skirling Pass"),
        (1, "The Hook"),
    ]

    # - Popping Heap:
    # Expecting: (1, 'The Hook')
    # Actual: (1, 'The Hook')
    #
    # - Popping Heap:
    # Expecting: (3, 'Kingsroad')
    # Actual: (3, 'Kingsroad')
    #
    # - Popping Heap:
    # Expecting: (5, 'Street of Steel')
    # Actual: (7, 'Skirling Pass')
    for priority, value in push_inputs:
        print(f'- Pushing "{value}" with priority {priority}')
        min_heap.push(priority, value)
    print(min_heap.elements)
    for _ in range(len(min_heap.elements)):
        result = min_heap.pop()
        print(result)


if __name__ == "__main__":
    main()
