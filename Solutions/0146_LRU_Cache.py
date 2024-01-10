class LRUCache:

    def __init__(self, capacity: int):
        self.stack_size = 0
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
            self.stack[key]=value
            self.stack.move_to_end(key)
        elif self.capacity == self.stack_size:
            self.stack.popitem(last=False)
            self.stack[key]=value
        else:
            self.stack_size += 1
            self.stack[key]=value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)