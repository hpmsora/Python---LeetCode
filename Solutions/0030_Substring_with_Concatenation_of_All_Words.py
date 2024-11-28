class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        words_dict = {}
        p_word_count = word_len * len(words)
        # Words dictionary
        for each_words in words:
            if each_words in words_dict:
                words_dict[each_words] += 1
            else:
                words_dict[each_words] = 1

        right = word_len - 1
        sol = []

        index = 0
        while index < word_len:
            # Declare new word dictionary
            new_word_dict = {}
            complete_set = set()
            right = word_len + index
            while right < len(s) + 1:
                first_word = s[right-word_len:right]
                next_right = right + word_len

                if first_word in words_dict:
                    # Init values
                    new_right = right
                    left = right-word_len

                    # Check validation
                    while new_right < len(s)+1:
                        first_word = s[left:left+word_len]
                        new_word = s[new_right-word_len:new_right]
                        if new_word in words_dict:
                            if new_word in new_word_dict:
                                new_word_dict[new_word] += 1
                            else:
                                new_word_dict[new_word] = 1
                            
                            if new_word_dict[new_word] == words_dict[new_word]:
                                complete_set.add(new_word)

                                if len(complete_set) == len(words_dict):
                                    sol.append(left)
                                if new_right - left == p_word_count:
                                    if first_word in complete_set:
                                        if first_word in new_word_dict and new_word_dict[first_word] == words_dict[first_word]:
                                            complete_set.remove(first_word)
                                    if new_word_dict[first_word] == 1:
                                        del new_word_dict[first_word]
                                    else:
                                        new_word_dict[first_word] -= 1
                                    left += word_len
                            else:
                                if new_right - left == p_word_count:
                                    if first_word in complete_set:
                                        if first_word in new_word_dict and new_word_dict[first_word] == words_dict[first_word]:
                                            complete_set.remove(first_word)
                                    if new_word_dict[first_word] == 1:
                                        del new_word_dict[first_word]
                                    else:
                                        new_word_dict[first_word] -= 1
                                    left += word_len
                        else:
                            new_word_dict = {}
                            complete_set = set()
                            left = new_right
                        new_right += word_len
                    right = next_right
                    break
                else:
                    right = next_right
            index += 1
            
        return sol