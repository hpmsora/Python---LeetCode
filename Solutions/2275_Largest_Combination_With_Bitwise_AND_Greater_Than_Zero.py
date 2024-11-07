class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        dict_can = {}

        for each_candidites in candidates:
            each_bin = bin(each_candidites)[2:]
            for index, each_binary in enumerate(each_bin[::-1]):
                if each_binary == "1":
                    if index in dict_can:
                        dict_can[index] += 1
                    else:
                         dict_can[index] = 1
        
        return max(dict_can.values())