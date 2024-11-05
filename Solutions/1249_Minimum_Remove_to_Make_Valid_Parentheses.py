class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sol = []

        open_par = []

        for index, each_s in enumerate(s):
            if each_s == "(":
                open_par.append(index)
            elif each_s == ")":
                if not open_par:
                    sol.append(index)
                else:
                    open_par.pop()

        s_list = list(s)
        for each_index in sol + open_par:
            s_list[each_index] = ""

        return ''.join(s_list)