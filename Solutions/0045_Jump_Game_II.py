class Solution:
    def jump(self, nums: List[int]) -> int:
        size_nums = len(nums)

        if size_nums == 1:
            return 0

        index = 0
        sol = 0
        max_index = 0

        while index < size_nums:
            curr = nums[index]

            temp_max_list = []
            if index + curr >= size_nums - 1:
                return sol + 1
            for temp_index in range(index + 1, index + curr + 1):
                temp_max_list.append((temp_index + nums[temp_index], temp_index))

            index = max(temp_max_list)[1]
            sol += 1
        return sol