class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        p_dict = {}
        p_list = []
        n_dict = {}
        n_list = []
        z_dict = {}
        
        for each_nums in nums:
            if each_nums == 0:
                if each_nums in z_dict:
                    z_dict[each_nums] += 1
                else:
                    z_dict[each_nums] = 1
            elif each_nums > 0:
                if each_nums in p_dict:
                    p_dict[each_nums] += 1
                else:
                    p_dict[each_nums] = 1
                    p_list.append(each_nums)
            else:
                if each_nums in n_dict:
                    n_dict[each_nums] += 1
                else:
                    n_dict[each_nums] = 1
                    n_list.append(each_nums)
        
        sol = []
        
        # 1. 0 + 0 + 0
        if z_dict and z_dict[0] >= 3:
            sol.append([0, 0, 0])
        # 2. p + n + 0
        if z_dict and z_dict[0] >= 1:
            for each_p_list in p_list:
                if each_p_list * -1 in n_dict:
                    sol.append([each_p_list, each_p_list*-1, 0])
        # 3. p + p + n
        for index, each_p_1 in enumerate(p_list):
            # same two p
            if p_dict[each_p_1] >= 2 and each_p_1*-2 in n_dict:
                sol.append([each_p_1, each_p_1, each_p_1*-2])
            for each_p_2 in p_list[index+1:]:
                if (each_p_1 + each_p_2) * -1 in n_dict:
                    sol.append([each_p_1, each_p_2, (each_p_1+each_p_2)*-1])
        # 4. n + n + p
        for index, each_n_1 in enumerate(n_list):
            # same two n
            if n_dict[each_n_1] >= 2 and each_n_1*-2 in p_dict:
                sol.append([each_n_1, each_n_1, each_n_1*-2])
            for each_n_2 in n_list[index+1:]:
                if (each_n_1 + each_n_2) * -1 in p_dict:
                    sol.append([each_n_1, each_n_2, (each_n_1+each_n_2)*-1])
                        
        return sol