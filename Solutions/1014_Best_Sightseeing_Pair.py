class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxVal = 0
        cur = 0            
        for i in range(1, len(values)):
            cur = max(cur, values[i-1]+i-1)
            maxVal = max(maxVal, cur+values[i]-i)
        return maxVal