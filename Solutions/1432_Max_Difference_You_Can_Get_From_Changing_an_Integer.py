class Solution:
    def maxDiff(self, num: int) -> int:
        max_swap = {}
        min_swap = {}

        # 1. Max Swap
        for digit in str(num):
            if not digit == "9":
                max_swap[digit] = "9"
                break
        
        # 2. Min Swap
        if str(num)[0] == "1":
            for digit in str(num)[1:]:
                if not digit == "0" and not digit == "1":
                    min_swap[digit] = "0"
                    break
        else:
            min_swap[str(num)[0]] = "1"
        
        # 3. Create Num
        max_num = ""
        min_num = ""
        for digit in str(num):
            if digit in min_swap:
                min_num += min_swap[digit]
            else:
                min_num += digit
            if digit in max_swap:
                max_num += max_swap[digit]
            else:
                max_num += digit
        
        # 4. Return
        return int(max_num) - int(min_num)