class Solution:
    def minSwaps(self, data: List[int]) -> int:
        k = sum(data) # window size 
        ans = val = 0 
        for i, x in enumerate(data): 
            val += x
            if i >= k: val -= data[i-k]
            if i+1 >= k: ans = max(ans, val)
        return k - ans