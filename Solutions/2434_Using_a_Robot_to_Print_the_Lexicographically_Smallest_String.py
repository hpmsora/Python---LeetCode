class Solution:
    def robotWithString(self, s: str) -> str:
        freq_dict = {}

        for each_s in s:
            if each_s in freq_dict:
                freq_dict[each_s] += 1
            else:
                freq_dict[each_s] = 1

        letter_list = []
        for letter_num in range(97, 123):
            letter = chr(letter_num)
            if letter in freq_dict:
                letter_list.append([letter, freq_dict[letter]])

        left_list = []
        sol = ""

        for each_s in s:
            if not letter_list:
                break
            if letter_list[0][0] == each_s:
                sol += each_s
                if letter_list[0][1] == 1:
                    letter_list.pop(0)
                else:
                    letter_list[0][1] -= 1
                # left_list polish
                if not letter_list:
                    break
                while left_list and left_list[-1] <= letter_list[0][0]:
                    sol += left_list.pop()
            else:
                index = 0
                while index < len(letter_list):
                    if letter_list[index][0] == each_s:
                        if letter_list[index][1] == 1:
                            letter_list.pop(index)
                        else:
                            letter_list[index][1] -= 1
                        break
                    index += 1
                left_list.append(each_s)
        
        sol += ''.join(left_list[::-1])
        return sol