class RingBuffer:
    def __init__(self, capacity):
        self.oldest = 0
        self.capacity = capacity
        # create a list of the length with None in all it fields
        self.buffer = [None] * self.capacity

    def append(self, item):
        self.buffer[self.oldest] = item
        self.oldest += 1
        self.oldest %= self.capacity 

    def get(self):
        output = []
        for item in self.buffer:
            if item is not None:
                output.append(item)
        return output