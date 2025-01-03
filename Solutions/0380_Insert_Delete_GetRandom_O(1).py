import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.num_index_dict = {}

    def insert(self, val: int) -> bool:
        if val in self.num_index_dict:
            return False
        self.nums.append(val)
        self.num_index_dict[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if not val in self.num_index_dict:
            return False
        index = self.num_index_dict[val]
        temp_nums = self.nums[-1]
        self.nums[index] = temp_nums
        self.num_index_dict[temp_nums] = index
        self.nums.pop()
        del self.num_index_dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()