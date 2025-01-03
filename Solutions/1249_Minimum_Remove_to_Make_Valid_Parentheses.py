class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        par_list = []

        for index, each_s in enumerate(s):
            if each_s == "(":
                par_list.append(("(", index))
            elif each_s == ")":
                if par_list and par_list[-1][0] == "(":
                    par_list.pop()
                else:
                    par_list.append((")", index))
        
        s_list = list(s)
        for _, index in par_list:
            s_list[index] = ""
        return ''.join(s_list)