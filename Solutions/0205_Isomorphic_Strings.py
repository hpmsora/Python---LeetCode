class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # s and t letter dict
        s_dict = {}
        t_set = set()

        # loop - all s and t letter
        for each_s, each_t in zip(s, t):
            if each_s in s_dict: # check letter s in s dictionary
                if not s_dict[each_s] == each_t:
                    # RETURN - not match
                    return False
            else:
                if each_t in t_set:
                    # RETURN - duplication
                    return False
                
                # update s_dict and s_set
                s_dict[each_s] = each_t
                t_set.add(each_t)
        # RETURN - pass all
        return True