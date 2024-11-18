class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        par_heap = []

        sol = []
        s_list = list(s)

        for index, each_s in enumerate(s_list):
            if each_s == "(":
                par_heap.append((each_s, index))
            
            elif each_s == ")":
                if par_heap and par_heap[-1][0] == "(":
                    par_heap.pop()
                    sol.append(index)
                else:
                    par_heap.append((each_s, index))
        for _, index in par_heap:
            s_list[index] = ""
        return "".join(s_list)