class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        else:
            sign = 1

        quotient = 0
        multiple = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        while dividend >= (divisor << 1): #dividend >= 2*divisor
            divisor <<= 1   #divisor *= 2
            multiple <<= 1  #multiple *= 2
        while multiple > 0:
            if dividend >= divisor:
                dividend -= divisor
                quotient += multiple
            divisor >>= 1   #divisor /= 2
            multiple >>= 1  #multiple /= 2
        
        return sign * quotient