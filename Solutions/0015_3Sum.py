class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. Distribute numbers to positive, negative, zeros
        # __dict => key: int(value), value: int(freq)
        p_dict = {}
        n_dict = {}
        z_dict = {}

        for each_nums in nums:
            if each_nums  == 0: # Zeros
                if each_nums in z_dict:
                    z_dict[each_nums] += 1
                else:
                    z_dict[each_nums] = 1
            elif each_nums < 0: # Negative
                if each_nums in n_dict:
                    n_dict[each_nums] += 1
                else:
                    n_dict[each_nums] = 1
            else: # Positive
                if each_nums in p_dict:
                    p_dict[each_nums] += 1
                else:
                    p_dict[each_nums] = 1

        # 2-0 Declare solution list
        sol = []
        # 2-1. 0 + 0 + 0
        if z_dict and z_dict[0] >= 3:
            sol.append([0, 0, 0])
        # 2-2. P + N + 0
        for each_p in p_dict.keys():
            if each_p * -1 in n_dict and z_dict:
                sol.append([each_p, each_p * -1, 0])
        # 2-3. P + P + N
        p_list = list(p_dict.keys())
        index = 0
        while index < len(p_list):
            each_p = p_list[index]
            freq = p_dict[each_p]
            # Special case: freq >= 2
            if freq >= 2:
                if each_p * -2 in n_dict:
                    sol.append([each_p, each_p, each_p*-2])
            for index_2 in range(index + 1, len(p_list)):
                if ((each_p + p_list[index_2]) * -1) in n_dict:
                    sol.append([each_p, p_list[index_2], (each_p + p_list[index_2]) * -1])
            index += 1
        # 2-4. N + N + P
        n_list = list(n_dict.keys())
        index = 0
        while index < len(n_list):
            each_n = n_list[index]
            freq = n_dict[each_n]
            # Special case: freq >= 2
            if freq >= 2:
                if each_n * -2 in p_dict:
                    sol.append([each_n, each_n, each_n*-2])
            for index_2 in range(index + 1, len(n_list)):
                if ((each_n + n_list[index_2]) * -1) in p_dict:
                    sol.append([each_n, n_list[index_2], (each_n + n_list[index_2]) * -1])
            index += 1
        
        # 3. RETURN solution
        return sol