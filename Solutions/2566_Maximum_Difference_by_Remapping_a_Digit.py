class Solution:
    def minMaxDifference(self, num: int) -> int:
        max_swap = {}
        min_swap = {}

        for digit in str(num):
            if not digit == "9":
                max_swap[digit] = "9"
                break

        min_digit = str(num)[0]
        min_swap[min_digit] = "0"

        max_num = ""
        min_num = ""
        for digit in str(num):
            if digit in max_swap:
                max_num += max_swap[digit]
            else:
                max_num += digit
            if digit in min_swap:
                min_num += min_swap[digit]
            else:
                min_num += digit
        max_num = int(max_num)
        min_num = int(min_num)
        return max_num - min_num