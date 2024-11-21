class Solution:

    def __init__(self, nums: List[int]):
        self.nums_index_freq_dict = {}
        for index, each_nums in enumerate(nums):
            if each_nums in self.nums_index_freq_dict:
                self.nums_index_freq_dict[each_nums].append(index)
            else:
                self.nums_index_freq_dict[each_nums] = [index]

    def pick(self, target: int) -> int:
        index_list = self.nums_index_freq_dict[target]
        new_index = math.floor(random.random() * len(index_list))
        
        return index_list[new_index]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)