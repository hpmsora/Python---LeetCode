class Solution:
    def pivotInteger(self, n: int) -> int:
        sum_n = sum(range(1, n+1))

        prev_sum = 0
        for each_n in range(1, n+1):
            current_sum = prev_sum + each_n

            if current_sum == sum_n - prev_sum:
                return each_n
            prev_sum = current_sum
        return -1