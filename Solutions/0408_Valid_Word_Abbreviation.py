class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        num = ''
        num_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        w_index = 0
        for index in range(len(abbr)):
            each_abbr = abbr[index]
            if each_abbr in num_set:
                if num == '' and each_abbr == '0':
                    return False
                num += each_abbr
            else:
                if not len(num) == 0:
                    w_index += int(num)
                    num = ''
                if w_index >= len(word):
                    return False
                if not word[w_index] == each_abbr:
                    return False
                else:
                    w_index += 1
        if not num == '':
            return w_index + int(num) == len(word)
        if w_index != len(word):
            return False
        return True