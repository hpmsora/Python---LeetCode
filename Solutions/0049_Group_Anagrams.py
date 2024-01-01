class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol_dict = {}

        for each_str in strs:
            str_sorted = ''.join(sorted(each_str))
            if each_str == "":
                str_sorted = ""

            if str_sorted in sol_dict:
                sol_dict[str_sorted].append(each_str)
            else:
                sol_dict[str_sorted] = [each_str]
        
        return sol_dict.values()