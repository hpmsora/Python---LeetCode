class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sorted = sorted(list(set(arr)))

        rank_dict = {}

        for index, each_arr_sorted in enumerate(arr_sorted):
            rank_dict[each_arr_sorted] = index + 1
        
        sol = []

        for each_arr in arr:
            sol.append(rank_dict[each_arr])
        
        return sol