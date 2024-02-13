class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_dict = {}
        for each_order in order:
            order_dict[each_order] = 0
        
        sol = ""
        for each_s in s:
            if each_s in order_dict:
                order_dict[each_s] += 1
            else:
                sol += each_s

        for key, val in reversed(order_dict.items()):
            if not val == 0:
                sol = key * val + sol
        return sol