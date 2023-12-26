class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        sol = []

        for index in range(1, len(mountain)-1):
            peak = max([mountain[index - 1], mountain[index], mountain[index + 1]])

            if not (peak == mountain[index + 1] or peak == mountain[index - 1]):
                sol.append(index)
        return sol