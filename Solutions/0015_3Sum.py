class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = set()
        
        p_list = []
        n_list = []
        z_list = []
        p_set = set()
        n_set = set()
        z_set = set()

        for num in nums:
            if num > 0:
                p_list.append(num)
                p_set.add(num)
            elif num < 0:
                n_list.append(num)
                n_set.add(num)
            else:
                z_list.append(num)
                z_set.add(num)

        if len(z_list) >= 3:
            sol.add(tuple([0, 0, 0]))

        len_p_list = len(p_list)
        len_n_list = len(n_list)

        if len(z_list) > 0:
            for each_p_set in p_set:
                if (-1 * each_p_set) in n_set:
                    sol.add(tuple([-1 * each_p_set, 0, each_p_set]))
        
        for i in range(len_p_list):
            for j in range(i + 1, len_p_list):
                num = -1 * (p_list[i] + p_list[j])
                if num in n_set:
                    sol.add(tuple(sorted([p_list[i], p_list[j], num])))
        
        for i in range(len_n_list):
            for j in range(i + 1, len_n_list):
                num = -1 * (n_list[i] + n_list[j])
                if num in p_set:
                    sol.add(tuple(sorted([n_list[i], n_list[j], num])))

        return [ list(x) for x in sol ]