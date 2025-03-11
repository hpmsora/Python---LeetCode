class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count_dict = {}
        sol = 0

        left = 0
        right = 0
        while right < len(s):
            right_letter = s[right]
            if right_letter in count_dict:
                count_dict[right_letter] += 1
            else:
                count_dict[right_letter] = 1

            if len(count_dict.keys()) == 3:
                sol += 1
            while len(count_dict.keys()) == 3 and left <= right - 3:
                left_letter = s[left]
                if left_letter in count_dict:
                    if count_dict[left_letter] == 1:
                        break
                        del count_dict[left_letter]
                    else:
                        count_dict[left_letter] -= 1
                left += 1
            sol += left
            right += 1
        return sol