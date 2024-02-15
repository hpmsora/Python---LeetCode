class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum_reminder_dict = {}

        prev_sum = 0

        for index, num in enumerate(nums):
            prev_sum += num

            reminder = prev_sum % k
            if index >= 1 and reminder == 0:
                return True

            if reminder in sum_reminder_dict:
                pre_index = sum_reminder_dict[reminder]
                if index - pre_index > 1:
                    return True
                else:
                    continue

            sum_reminder_dict[reminder] = index
        return False