class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sol = ""
        if len(a) > len(b):
            b = "0"*(len(a) - len(b)) + b
        elif len(b) > len(a):
            a = "0"*(len(b) - len(a)) + a
        
        carry = 0
        for each_a, each_b in zip(reversed(a), reversed(b)):
            sum_a_b = int(each_a) + int(each_b) + carry

            carry = int(sum_a_b / 2)
            sum_a_b = int(sum_a_b % 2)

            sol = str(sum_a_b) + sol
        
        if not carry == 0:
            sol = str(carry) + sol
        return sol