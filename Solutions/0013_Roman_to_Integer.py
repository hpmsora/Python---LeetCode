class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        total = 0
        pre_digit = roman_dict[s[0]]
        for each_digit in s:
            value = roman_dict[each_digit]
            if value <= pre_digit:
                total += value
            else:
                total += value
                total -= 2*pre_digit
            pre_digit = value
        return total