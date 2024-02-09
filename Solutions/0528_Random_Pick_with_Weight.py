class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        w_sum = sum(w)
        self.s_percent_gap = []
        total = 0
        for each_w in w:
            gap_percent = each_w/w_sum + total
            self.s_percent_gap.append(gap_percent)
            total = gap_percent
        print(self.s_percent_gap)

    def pickIndex(self) -> int:
        rd = random.random()
        
        index = 0
        for index, each_gap in enumerate(self.s_percent_gap):
            if rd <= each_gap:
                return index
        return len(self.w) - 1
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()