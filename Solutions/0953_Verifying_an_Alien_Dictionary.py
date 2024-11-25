class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict_letter_index = {}
        
        for index, each_order in enumerate(order):
            order_dict_letter_index[each_order] = index
            
        if len(words) == 1:
            return True
        
        pre_words = words[0]
        
        for each_words in words[1:]:
            index = 0
            min_len = min(len(pre_words), len(each_words))
            isInOrder = False
            while index < min_len:
                if order_dict_letter_index[pre_words[index]] > order_dict_letter_index[each_words[index]]:
                    return False
                elif order_dict_letter_index[pre_words[index]] < order_dict_letter_index[each_words[index]]:
                    isInOrder = True
                    break
                index += 1
            
            if not isInOrder and len(pre_words) > len(each_words):
                return False
            pre_words = each_words
        return True