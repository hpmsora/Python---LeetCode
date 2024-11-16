class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        left = float('inf')
        right = 0

        prev_arr = arr[0]
        for index, each_arr in enumerate(arr[1:]):
            if prev_arr > each_arr:
                left = min(left, index)
                right = max(right, index+1)
            prev_arr = each_arr
        if left == float('inf'):
            return 0
        
        arr_left = arr[:left+1]
        arr_right = arr[right:]

        iter_arr = arr_left
        search_arr = arr_right

        min_sol = min(len(iter_arr), len(search_arr))

        last_index_2 = 0
        for index, each_search_arr in enumerate(search_arr):
            index_2 = last_index_2
            while index_2 < len(iter_arr) and iter_arr[index_2] <= each_search_arr:
                min_sol = min(min_sol, len(iter_arr) - index_2 - 1 + index)
                last_index_2 = index_2
                index_2 += 1
            if not iter_arr:
                break
            if min_sol <= index:
                break

        return right - left - 1 + min_sol