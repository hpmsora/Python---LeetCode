class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left, right = 0, 0

        freq_dict = {}
        sol = 0

        while right < len(nums):
            new_num = nums[right]

            if new_num in freq_dict:
                freq_dict[new_num] += 1

                if freq_dict[new_num] > k:
                    while freq_dict[new_num] > k and right >= left:
                        left_num = nums[left]
                        freq_dict[left_num] -= 1
                        if freq_dict[left_num] == 0:
                            del freq_dict[left_num]
                        left += 1
            else:
                freq_dict[new_num] = 1

            sol = max(sol, right - left + 1)

            right += 1

        return sol