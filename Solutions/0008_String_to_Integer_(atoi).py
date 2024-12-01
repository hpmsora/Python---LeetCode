class Solution:
    def myAtoi(self, s: str) -> int:
        nums_set = set(
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        )

        if not s:
            return 0

        isNegative = False
        for index, each_s in enumerate(s):
            if each_s.isalnum() or each_s == "-" or each_s == "+":
                if each_s == "+" or each_s == "-":
                    if index < len(s)-1:
                        if s[index + 1] in nums_set:
                            continue
                        else:
                            return 0
                    return 0
                elif not each_s in nums_set:
                    return 0
            elif each_s == " ":
                continue
            else:
                return 0
            if each_s in nums_set:
                nums = each_s
                if index > 0 and s[index-1] == "-":
                    isNegative = True
                index += 1
                while index < len(s):
                    if s[index] in nums_set:
                        nums += s[index]
                    else:
                        break
                    index += 1
                nums_int = int(nums)
                if isNegative:
                    if int(nums) > 2**31:
                        return -1 * 2**31
                    return -1 * nums_int
                else:
                    if int(nums) > 2**31-1:
                        return 2**31 -1
                    return nums_int
        return 0