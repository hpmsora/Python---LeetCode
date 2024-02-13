class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.nums_dict = {}
        for index, num in enumerate(nums):
            if num in self.nums_dict:
                self.nums_dict[num].append(index)
            else:
                self.nums_dict[num] = [index]

    def pick(self, target: int) -> int:
        index_list = self.nums_dict[target]
        index_list_size = len(index_list)
        
        rand = random.random()
        
        index = int(rand // (1/index_list_size))
        return index_list[index]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)