class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift_list = [0] * len(s)

        num_to_chr = {}
        chr_to_num = {}
        for num in range(97, 123):
            num_to_chr[num-97] = chr(num)
            chr_to_num[chr(num)] = num-97

        for start, end, dire in shifts:
            if dire == 0:
                shift_list[start] -= 1
            else:
                shift_list[start] += 1
            if end + 1 < len(s):
                if dire == 0:
                    shift_list[end+1] += 1
                else:
                    shift_list[end+1] -= 1

        s_list = list(s)
        new_order = 0
        for index, each_shift in enumerate(shift_list):
            new_order += each_shift
            curr_letter = s_list[index]

            new_num = (chr_to_num[curr_letter] + new_order) % 26
            if new_num >= 0:
                s_list[index] = num_to_chr[new_num]
            else:
                s_list[index] = num_to_chr[new_num+26]
        return "".join(s_list)