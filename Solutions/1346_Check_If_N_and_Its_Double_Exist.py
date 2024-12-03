class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_freq_dict = {}

        for each_arr in arr:
            if each_arr in arr_freq_dict:
                arr_freq_dict[each_arr] += 1
            else:
                arr_freq_dict[each_arr] = 1

        for each_arr_set in arr_freq_dict:
            if each_arr_set * 2 in arr_freq_dict:
                if each_arr_set == each_arr_set * 2:
                    if arr_freq_dict[each_arr_set] >= 2:
                        return True
                    else:
                        continue
                else:
                    return True
                
        return False