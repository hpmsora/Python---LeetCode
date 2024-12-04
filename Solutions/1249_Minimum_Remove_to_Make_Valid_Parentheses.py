class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        s_list = list(s)
        par_list = []
        for index, each_s in enumerate(s_list):
            if each_s == "(":
                par_list.append(("(", index))
            elif each_s  == ")":
                if par_list and par_list[-1][0] == "(":
                    par_list.pop()
                else:
                    par_list.append((")", index))
        
        for _, index in par_list:
            s_list[index] = ""
        
        return ''.join(s_list)