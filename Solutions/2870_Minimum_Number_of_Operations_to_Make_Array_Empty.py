class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num_dict = {}

        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        
        sol = 0
        for val in num_dict.values():
            if val == 1:
                return -1
            else:
                sol += int(val / 3)
                if not val % 3 == 0:
                    sol += 1
        return sol