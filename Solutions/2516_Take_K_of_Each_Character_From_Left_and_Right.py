class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if len(s) < k*3:
            return -1
        if k == 0:
            return 0
        sol = 0

        left_dict = {'a': 0, 'b': 0, 'c': 0}

        s_list = list(s)
        right_dict = {'a': 0, 'b': 0, 'c': 0}
        right_min_index = -1

        for index, each_s in enumerate(s_list[::-1]):
            index = len(s_list) - index - 1
            right_dict[each_s] += 1
            if right_dict['a'] >= k and right_dict['b'] >= k and right_dict['c'] >= k:
                right_min_index = index
                break
        if right_min_index == -1:
            return -1
        sol = len(s_list) - right_min_index
        
        for index, each_s in enumerate(s_list):
            left_dict[each_s] += 1

            if left_dict['a'] >= k and left_dict['b'] >= k and left_dict['c'] >= k:
                sol = min(sol, index + 1)
                break
            
            if each_s == s_list[right_min_index]:
                right_min_index += 1
                right_dict[each_s] -= 1
                while left_dict['a'] + right_dict['a'] >= k and left_dict['b'] + right_dict['b'] >= k and left_dict['c'] + right_dict['c'] >= k:
 
                    right_dict[s_list[right_min_index]] -= 1
                    right_min_index += 1
                right_min_index -= 1
                right_dict[s_list[right_min_index]] += 1

                sol = min(sol, index + 1 + len(s_list) - right_min_index)
        return sol