class Solution:
    def minimumSteps(self, s: str) -> int:
        swap = 0
        skip = 0

        for each_s in s:
            if each_s == "0":
                swap += skip
            else:
                skip += 1
        return swap