class Solution:

    def __init__(self, nums: List[int]):
        # Declare dictionary (key: num, value: [index, ...])
        self.dict_index = {}

        # Loop - each nums
        for index, each_num in enumerate(nums):
            # Update index dictionary
            if each_num in self.dict_index:
                self.dict_index[each_num].append(index)
            else:
                self.dict_index[each_num] = [index]

    def pick(self, target: int) -> int:
        # Get index list
        index_list = self.dict_index[target]

        # RETURN - random index
        return random.choice(index_list)

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)