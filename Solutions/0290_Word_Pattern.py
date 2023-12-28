class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")

        if not len(pattern) == len(s_list):
            return False
        
        pattern_dict = {}
        s_set = set()
        for each_pattern, each_s_list in zip(pattern, s_list):
            if each_pattern in pattern_dict:
                if not each_s_list == pattern_dict[each_pattern]:
                    return False
            else:
                if each_s_list in s_set:
                    return False
                s_set.add(each_s_list)
                pattern_dict[each_pattern] = each_s_list
        return True