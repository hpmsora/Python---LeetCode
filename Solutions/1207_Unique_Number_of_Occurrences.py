class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_count_dict = {}

        for num in arr:
            if num in arr_count_dict:
                arr_count_dict[num] += 1
            else:
                arr_count_dict[num] = 1
            
        num_set = set()

        for value in arr_count_dict.values():
            if value in num_set:
                return False
            else:
                num_set.add(value)
        
        return True