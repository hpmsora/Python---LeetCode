class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        abbr_list = []
        # Loop - abbr
        index = 0
        number = set(["1","2","3","4","5","6","7","8","9","0"]) # number specification
        while index < len(abbr):
            # Get indexed letter
            letter = abbr[index]
            # Check letter is number
            if letter in number:
                # number start with 0, return False
                if letter == "0":
                    return False
                # Check connected number
                index += 1
                while index < len(abbr):
                    letter_2 = abbr[index]
                    if letter_2 in number:
                        letter += letter_2
                        index += 1
                    else:
                        index -= 1
                        break
                # Add number
                abbr_list.append((True, int(letter)))
            else:
                # Add letter
                abbr_list.append((False, letter))
            index += 1

        # Loop - abbr list
        index = 0
        index_abbr_list = 0
        for isNumber, each_abbr_list in abbr_list:
            # Check matching with number
            if index > len(word) - 1:
                return False
            if isNumber:
                index += each_abbr_list
                if index > len(word):
                    return False
                elif index == len(word) and index_abbr_list == len(abbr_list)-1:
                    return True
                continue
            elif not word[index] == each_abbr_list:
                return False
            index += 1
            index_abbr_list += 1
        
        # RETURN - pass all test
        if index == len(word):
            return True
        else:
            return False