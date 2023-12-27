class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        len_digits = len(digits)
        digits[-1] = digits[-1] + 1
        carry = int(digits[-1] / 10)
        digits[-1] = digits[-1] % 10
        for index in range(len_digits - 2, -1, -1):
            print(carry)
            if carry == 0:
                break
            digits[index] = digits[index] + carry
            carry = int(digits[index] / 10)
            digits[index] = digits[index] % 10
        if carry == 1:
            digits = [1] + digits
        return digits