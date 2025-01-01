class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        shift_left = 0

        for direction, amount in shift:
            if direction == 0:
                shift_left += amount
            else:
                shift_left -= amount
        shift_left %= len(s)
        if shift_left >= 0:
            return s[shift_left:] + s[:shift_left]
        else:
            shift_left = len(s) + shift_left
            return s[shift_left:] + s[:shift_left]