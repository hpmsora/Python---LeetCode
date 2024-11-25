class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sol = 0
        max_negative = float('-inf')
        max_negative_num = 0
        min_positive = float('inf')
        isZero = False
        for each_m in matrix:
            for each_n in each_m:
                if each_n < 0:
                    max_negative_num += 1
                    sol += -1 * each_n
                    if max_negative < each_n:
                        max_negative = each_n
                elif each_n == 0:
                    isZero = True
                else:
                    if min_positive > each_n:
                        min_positive = each_n
                    sol += each_n

        if isZero:
            return sol
        elif max_negative_num % 2 == 1:
            return max(sol + max_negative * 2, sol - min_positive * 2)
        else:
            return sol