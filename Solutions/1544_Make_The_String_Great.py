class Solution:
    def makeGood(self, s: str) -> str:
        index = 0
        s_list = list(s)

        while index < len(s_list):
            letter = s_list[index]
            if index < len(s_list) - 1:
                letter_next = s_list[index + 1]
                if letter.lower() == letter_next.lower():
                    if (letter.islower() and letter_next.isupper()) or (letter.isupper() and letter_next.islower()):
                        s_list.pop(index)
                        s_list.pop(index)
                        if not index == 0:
                            index -= 1
                        continue

            index += 1

        return ''.join(s_list)