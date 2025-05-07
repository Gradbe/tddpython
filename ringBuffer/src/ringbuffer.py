class RingBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.index = 0

    def add(self, element):
        self.buffer[self.index] = element
        self.index = (self.index + 1) % self.size
    
    def get(self):
        return self.buffer

