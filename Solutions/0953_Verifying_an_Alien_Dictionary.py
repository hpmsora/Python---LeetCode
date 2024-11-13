class Solution:
    def isInOrder(self, _word_1, _word_2, _letter_order_dict):
        index = 0
        
        min_len = min(len(_word_1), len(_word_2))
        
        while index < min_len:
            letter_1 = _word_1[index]
            letter_2 = _word_2[index]
            if not letter_1 == letter_2:
                if _letter_order_dict[letter_1] < _letter_order_dict[letter_2]:
                    return True
                else:
                    return False
            index += 1
        if len(_word_1) <= len(_word_2):
            return True
        else:
            return False
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        
        letter_order_dict = {}
        
        for index, each_order in enumerate(order):
            letter_order_dict[each_order] = index
        
        index = 1
        
        while index < len(words):
            prev_word = words[index-1]
            curr_word = words[index]
            
            if not self.isInOrder(prev_word, curr_word, letter_order_dict):
                return False
            index += 1
        return True