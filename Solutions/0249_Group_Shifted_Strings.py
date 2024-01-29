class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def helper(_string):
            diff_list = "0"
            prev = ord(_string[0]) - 97
            for letter in _string[1:]:
                cur_num = (ord(letter) - 97)
                diff = prev - cur_num
                if diff < 0:
                    diff = 26 + diff
                diff_list += "-" + str(diff)
                prev = cur_num
            return diff_list

        sol_dict = {}
        for string in strings:
            diff_list = helper(string)
            if diff_list in sol_dict:
                sol_dict[diff_list].append(string)
            else:
                sol_dict[diff_list] = [string]

        sol = []

        for val in sol_dict.values():
            sol.append(val)

        return sol