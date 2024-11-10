class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        sol = 0
        
        dp = [{} for _ in range(len(nums))]
        
        for index, each_nums in enumerate(nums[::-1]):
            index = len(nums) - index - 1
            
            index_2 = index
            count = 1
            index_2 += 1
            max_count = 2
            while index_2 < len(nums):
                diff = each_nums - nums[index_2]
                max_count_index_2 = 2
                if diff in dp[index_2]:
                    if diff in dp[index]:
                        max_count_index_2 = max(dp[index][diff], dp[index_2][diff] + 1)
                        dp[index][diff] = max_count_index_2
                    else:
                        max_count_index_2 = dp[index_2][diff] + 1
                        dp[index][diff] = max_count_index_2
                else:
                    if diff in dp[index]:
                        dp[index][diff] = max(dp[index][diff], 2)
                    else:
                        dp[index][diff] = 2
                max_count = max(max_count, max_count_index_2)
                index_2 += 1
            sol = max(sol, max_count)
                
        return sol