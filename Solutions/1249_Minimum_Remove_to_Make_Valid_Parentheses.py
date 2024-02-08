class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        par_list = []

        remove_list = set()
        for index in range(len(s)):
            each_s = s[index]
            if each_s == "(":
                par_list.append(("(", index))
            elif each_s == ")":
                if not par_list:
                    remove_list.add(index)
                    continue
                
                par_list.pop()
        for _, index in par_list:
            remove_list.add(index)

        sol = ""
        for index in range(len(s)):
            each_s = s[index]
            if not index in remove_list:
                sol += each_s
        return sol