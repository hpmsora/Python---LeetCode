class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def b_str(_s):
            inv_s = ""
            for each_s in _s:
                if each_s == "1":
                    inv_s += "0"
                else:
                    inv_s += "1"
            return _s + "1" + inv_s[::-1]
        
        new_s = "0"
        while n > 0 and len(new_s) < k * 2:
            new_s = b_str(new_s)
            n -= 1
        
        return new_s[k-1]