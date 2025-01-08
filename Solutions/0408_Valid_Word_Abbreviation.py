class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        num_set = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        abbr_list = []
        num = ""
        for each_abbr in abbr:
            if each_abbr in num_set:
                if not num and each_abbr == "0":
                    return False
                num += each_abbr
            else:
                if num:
                    abbr_list.append((1, int(num)))
                    num = ""
                abbr_list.append((0, each_abbr))
        if num:
            abbr_list.append((1, int(num)))

        print(abbr_list)

        index_word = 0
        for isStrNum, each_abbr_list in abbr_list:
            if isStrNum == 0:
                if index_word >= len(word) or not word[index_word] == each_abbr_list:
                    return False
                else:
                    index_word += 1
            else:
                index_word += each_abbr_list
                if index_word > len(word):
                    return False
        if index_word == len(word):
            return True
        else:
            return False