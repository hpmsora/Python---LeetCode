class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        nums = set()

        for each_left, each_right in intervals:
            for num in range(each_left, each_right):
                nums.add(num)
                nums.add(num + 0.5)
            nums.add(each_right)
        
        nums = sorted(list(nums))

        left_num = 0
        right_num = 0
        sol = []
        if nums:
            left_num = nums.pop(0)
            right_num = left_num
        while nums:
            each_nums = nums.pop(0)
            if each_nums == right_num + 0.5:
                nums.pop(0)
                right_num += 1
            else:
                sol.append([left_num, right_num])
                left_num = each_nums
                right_num = each_nums
        sol.append([left_num, right_num])
        return sol