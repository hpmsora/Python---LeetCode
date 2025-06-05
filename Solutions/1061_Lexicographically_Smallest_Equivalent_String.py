class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        letter_set_list = []
        for each_s1, each_s2 in zip(s1, s2):
            index = 0
            temp_letter_list = []
            while index < len(letter_set_list):
                if each_s1 in letter_set_list[index] or each_s2 in letter_set_list[index]:
                    temp_letter_list.append(letter_set_list.pop(index))
                else:
                    index += 1
            if not temp_letter_list:
                letter_set_list.append(set([each_s1, each_s2]))
            else:
                new_set = set()
                for each_temp_letter_list in temp_letter_list:
                    new_set = new_set.union(each_temp_letter_list)
                new_set.add(each_s1)
                new_set.add(each_s2)
                letter_set_list.append(new_set)
        letter_smallest_dict = {}
        for each_letter_set_list in letter_set_list:
            smallest_letter = min(list(each_letter_set_list))
            for each_letter in each_letter_set_list:
                letter_smallest_dict[each_letter] = smallest_letter
        
        sol = ""
        for each_letter in baseStr:
            if each_letter in letter_smallest_dict:
                sol += letter_smallest_dict[each_letter]
            else:
                sol += each_letter
        return sol