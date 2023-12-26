class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        sol = []

        temp_num_left = 0
        temp_num_right = 0
        if len(nums) > 0:
            temp_num_left = nums.pop(0)
            temp_num_right = temp_num_left
        else:
            return []
        while nums:
            num = nums.pop(0)
            if not num == temp_num_right + 1:
                if not temp_num_left == temp_num_right:
                    sol.append(str(temp_num_left) + "->" + str(temp_num_right))
                else:
                    sol.append(str(temp_num_left))
                temp_num_left = num
                temp_num_right = num
            else:
                temp_num_right = num
        if temp_num_left == temp_num_right:
            sol.append(str(temp_num_left))
        else:
            sol.append(str(temp_num_left) + "->" + str(temp_num_right))
        return sol