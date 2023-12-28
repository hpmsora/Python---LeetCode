class Solution:
    def isHappy(self, n: int) -> bool:
        stop_list = set()
        if n == 1:
            return True
        while not n in stop_list:
            sum = 0
            stop_list.add(n)
            while n > 0:
                sum += (n % 10)**2
                n = int(n/10)
            n = sum
            if n == 1:
                return True
        return False