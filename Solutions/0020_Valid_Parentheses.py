class Solution:
    def isValid(self, s: str) -> bool:
        par_close_set = set([')', '}', ']'])
        par_pair = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        p_list = []

        for letter in s:
            if letter in par_pair:
                p_list.append(letter)
            elif letter in par_close_set:
                if p_list and par_pair[p_list[-1]] == letter:
                    p_list.pop()
                else:
                    return False
        if len(p_list) >= 1:
            return False
        return True