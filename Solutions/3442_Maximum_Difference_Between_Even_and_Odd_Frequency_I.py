class Solution:
    def maxDifference(self, s: str) -> int:
        s_count = Counter(s)

        odd = 0
        even = float('inf')
        for freq in s_count.values():
            if freq % 2 == 1:
                odd = max(odd, freq)
            else:
                even = min(even, freq)
        return odd - even