class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sub_sum = sum(nums[:k])
        sub_dict = {}
        more_than_2_list = set()
        for each_nums in nums[:k]:
            if each_nums in sub_dict:
                sub_dict[each_nums] += 1
                more_than_2_list.add(each_nums)
            else:
                sub_dict[each_nums] = 1
        if not more_than_2_list:
            sol = sub_sum
        else:
            sol = 0

        for index, each_nums in enumerate(nums[k:]):
            sub_sum = sub_sum - nums[index] + each_nums
            if sub_dict[nums[index]] == 1:
                del sub_dict[nums[index]]
            elif sub_dict[nums[index]] == 2:
                more_than_2_list.remove(nums[index])
                sub_dict[nums[index]] -= 1
            else:
                sub_dict[nums[index]] -= 1
            
            if each_nums in sub_dict:
                if sub_dict[each_nums] == 1:
                    more_than_2_list.add(each_nums)
                sub_dict[each_nums] += 1
            else:
                sub_dict[each_nums] = 1
            if not more_than_2_list:
                sol = max(sol, sub_sum)
        return sol