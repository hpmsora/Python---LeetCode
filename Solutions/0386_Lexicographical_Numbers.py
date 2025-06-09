class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        sol = []

        def helper(_num):
            if _num <= n:
                sol.append(_num)
            else:
                return
            for each_num in range(10):
                new_num = _num * 10 + each_num
                helper(new_num)
        
        for each_num in range(1,10):
            helper(each_num)
        
        return sol