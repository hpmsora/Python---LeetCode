class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # solution list
        par_list = []

        # removed set
        remove_list = set()

        # loop - all letter s
        for index in range(len(s)):
            # get left side letter
            each_s = s[index]

            if each_s == "(": # check open
                par_list.append(("(", index))
            elif each_s == ")": # check close
                if not par_list:
                    remove_list.add(index)
                    continue
                
                # remove
                par_list.pop()
        
        # loop - remove the letter
        for _, index in par_list:
            remove_list.add(index)

        # solution string
        sol = ""

        # loop - all letter s
        for index in range(len(s)):
            # get each letter
            each_s = s[index]
            if not index in remove_list:
                sol += each_s
        
        # RETURN - solution strig
        return sol