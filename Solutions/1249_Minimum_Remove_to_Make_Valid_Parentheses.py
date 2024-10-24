class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # declare par index list
        par_list = []
        # [("( or )", index), ...]

        # Loop - all letter in s
        for index, each_s in enumerate(s):
            # Check "("
            if each_s == "(":
                par_list.append(("(", index))
            # Check ")"
            elif each_s == ")":
                # Check removable
                if par_list and par_list[-1][0] == "(":
                    par_list.pop()
                else:
                    par_list.append((")", index))

        # Get set of unnecessay index set
        sol = ""
        index_set = set()
        for _, index in par_list:
            index_set.add(index)
        
        # Get removed string
        for index, each_s in enumerate(s):
            if not index in index_set:
                sol += each_s
        
        # RETURN
        return sol