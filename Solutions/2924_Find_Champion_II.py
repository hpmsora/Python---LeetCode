class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        stronger_list = [False] * n

        for weaker, stronger in edges:
            stronger_list[stronger] = True
        
        strongest = -1
        for index, each_stronger_list in enumerate(stronger_list):
            if not each_stronger_list:
                if not strongest == -1:
                    return -1
                strongest = index
        return strongest