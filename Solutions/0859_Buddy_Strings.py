class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if not len(s) == len(goal):
            return False
        s_1 = ""
        g_1 = ""
        s_2 = ""
        g_2 = ""
        
        diff_count = 0
        dup_set = set()
        isDup = False
        for each_s, each_g in zip(s, goal):
            if not each_s == each_g:
                if diff_count == 0:
                    s_1 = each_s
                    g_1 = each_g
                    diff_count += 1
                elif diff_count == 1:
                    s_2 = each_s
                    g_2 = each_g
                    diff_count += 1
                else:
                    return False
            else:
                if not isDup:
                    if each_s in dup_set:
                        isDup = True
                    else:
                        dup_set.add(each_s)

        if s_1 == g_2 and s_2 == g_1:
            if diff_count == 0:
                return isDup
            return True
        else:
            return False