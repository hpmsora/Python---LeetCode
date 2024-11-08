class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        arr2_set = set(arr2)
        arr3_set = set(arr3)

        sol = []
        for each_arr1 in arr1:
            if each_arr1 in arr2_set and each_arr1 in arr3_set:
                sol.append(each_arr1)
        
        return sol