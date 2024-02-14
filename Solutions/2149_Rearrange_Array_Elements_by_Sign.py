class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p_list = []
        n_list = []

        for num in nums:
            if num >= 0:
                p_list.append(num)
            else:
                n_list.append(num)
            
        sol = []
        for p_num, n_num in zip(p_list, n_list):
            sol += [p_num, n_num]
        
        return sol