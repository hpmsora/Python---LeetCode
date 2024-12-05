class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        elif n == 0:
            return 1
        elif n == -1:
            return 1/x
        
        else:
            if n % 2 == 1:
                return self.myPow(x * x, n // 2) * x
            else:
                return self.myPow(x * x, n // 2)