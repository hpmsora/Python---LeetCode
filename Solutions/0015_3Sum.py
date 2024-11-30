class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        p_freq = {}
        p_list = []
        n_freq = {}
        n_list = []
        z_freq = {}
        
        for each_nums in nums:
            if each_nums > 0:
                if each_nums in p_freq:
                    p_freq[each_nums] += 1
                else:
                    p_freq[each_nums] = 1
                    p_list.append(each_nums)
            elif each_nums == 0:
                if each_nums in z_freq:
                    z_freq[each_nums] += 1
                else:
                    z_freq[each_nums] = 1
            else:
                if each_nums in n_freq:
                    n_freq[each_nums] += 1
                else:
                    n_freq[each_nums] = 1
                    n_list.append(each_nums)
        
        # solution variable
        sol = []
        
        # 1. 0 + 0 + 0
        if 0 in z_freq and z_freq[0] >= 3:
            sol.append([0, 0, 0])
        # 2. 0 + P + N
        if 0 in z_freq and z_freq[0] >= 1:
            for each_p in p_freq.keys():
                if each_p * -1 in n_freq:
                    sol.append([0, each_p, -1 * each_p])
        # 3. P1 + P2 + N
        for index, each_p1 in enumerate(p_list):
            # 3.1 P1 == P2
            if p_freq[each_p1] >= 2 and each_p1 * -2 in n_freq:
                sol.append([each_p1, each_p1, -2 * each_p1])
            if index < len(p_list) - 1:
                for each_p2 in p_list[index+1:]:
                    if (each_p1 + each_p2) * -1 in n_freq:
                        sol.append([each_p1, each_p2, (each_p1 + each_p2) * -1])
        # 4. N1 + N2 + P
        for index, each_n1 in enumerate(n_list):
            # 3.1 N1 == N2
            if n_freq[each_n1] >= 2 and each_n1 * -2 in p_freq:
                sol.append([each_n1, each_n1, -2 * each_n1])
            if index < len(n_list) - 1:
                for each_n2 in n_list[index+1:]:
                    if (each_n1 + each_n2) * -1 in p_freq:
                        sol.append([each_n1, each_n2, (each_n1 + each_n2) * -1])
        # RETURN
        return sol