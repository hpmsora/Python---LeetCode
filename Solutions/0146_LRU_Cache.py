class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.stack = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.stack:
            self.stack.move_to_end(key)
            return self.stack[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.stack:
            self.stack.move_to_end(key)
            self.stack[key] = value
        elif self.size == self.capacity:
            self.stack.popitem(last=False)
            self.stack[key] = value
        else:
            self.stack[key] = value
            self.size += 1



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)