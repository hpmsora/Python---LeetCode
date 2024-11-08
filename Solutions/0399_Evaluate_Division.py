class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        cal_dict = {}
        last_var_set = set()

        for (numer, denom), value in zip(equations, values):
            if numer in cal_dict:
                cal_dict[numer][denom] = value
            else:
                cal_dict[numer] = {denom: value}
            if denom in cal_dict:
                cal_dict[denom][numer] = 1/value
            else:
                cal_dict[denom] = {numer: 1/value}
            last_var_set.add(denom)
            last_var_set.add(numer)
        print(cal_dict)

        sol = []

        for numer, denom in queries:
            # 1. value not exist
            if numer == denom and numer in cal_dict:
                sol.append(1.0)

            # 2. value same
            elif (not numer in cal_dict) or (not denom in last_var_set):
                sol.append(-1.0)
            
            # 3. rest
            else:
                seen = set()
                seen.add(numer)

                dp = []
                for each_keys, each_value in cal_dict[numer].items():
                    if each_keys == denom:
                        sol.append(each_value)
                        dp = []
                        break
                    dp.append((each_keys, each_value))
                if not dp:
                    continue
                
                isFeasible = False
                while dp:
                    each_dp, each_dp_value = dp.pop(0)
                    if not each_dp in seen and each_dp in cal_dict:
                        for each_keys, each_value in cal_dict[each_dp].items():
                            if each_keys == denom:
                                sol.append(each_value * each_dp_value)
                                dp = []
                                isFeasible = True
                                break
                            else:
                                if not each_keys in seen:
                                    dp.append((each_keys, each_value * each_dp_value))
                        seen.add(each_dp) 
                if not isFeasible:
                    sol.append(-1.0)
                
        return sol