class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        str_x = ""
        if x < 0:
            isNegative = True
            str_x = str(x*-1)
        else:
            str_x = str(x)

        str_sol = []
        for each_str_x in reversed(str_x):
            str_sol.append(each_str_x)

        if isNegative:
            str_sol = ['-'] + str_sol
            l_min_str = str(-1*(2**31))
            if len(str_sol) < len(l_min_str):
                return int(''.join(str_sol))
            elif len(str_sol) == len(l_min_str):
                for each_sol, each_l_min in zip(str_sol[1:], l_min_str[1:]):
                    if each_l_min < each_sol:
                        return 0
                    elif each_l_min == each_sol:
                        continue
                    else:
                        return int(''.join(str_sol))
            else:
                return 0
        else:
            str_sol = str_sol
            l_max_str = str(2**31 - 1)
            if len(str_sol) < len(l_max_str):
                return int(''.join(str_sol))
            elif len(str_sol) == len(l_max_str):
                for each_sol, each_l_max in zip(str_sol, l_max_str):
                    if each_l_max < each_sol:
                        return 0
                    elif each_l_max == each_sol:
                        continue
                    else:
                        return int(''.join(str_sol))
            else:
                return 0