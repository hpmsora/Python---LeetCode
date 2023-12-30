class RandomizedSet:

    def __init__(self):
        self.root = set()

    def insert(self, val: int) -> bool:
        if not val in self.root:
            self.root.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if not val in self.root:
            return False
        else:
            self.root.remove(val)
            return True

    def getRandom(self) -> int:
        return random.choice(list(self.root))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()