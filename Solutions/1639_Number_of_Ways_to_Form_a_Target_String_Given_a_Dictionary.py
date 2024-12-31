class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        target_dp = [0 for _ in target]

        target_dict = {}
        for index, each_target_letter in enumerate(list(target)):
            if each_target_letter in target_dict:
                target_dict[each_target_letter].append(index)
            else:
                target_dict[each_target_letter] = [index]

        for index in range(len(words[0])):
            letter_dict = {}
            for each_words in words:
                each_letter = each_words[index]

                if not each_letter in target_dict:
                    continue
                elif each_letter in letter_dict:
                    letter_dict[each_letter] += 1
                else:
                    letter_dict[each_letter] = 1

            update_dict = {}

            for key, freq in letter_dict.items():
                target_index_list = target_dict[key]
                for each_target_index_list in target_index_list:
                    if each_target_index_list == 0:
                        update_dict[0] = target_dp[0] + freq
                    else:
                        if not target_dp[each_target_index_list-1] == 0:
                            update_dict[each_target_index_list] = target_dp[each_target_index_list] + target_dp[each_target_index_list-1] * freq
            
            for key, updates in update_dict.items():
                target_dp[key] = updates
        return target_dp[-1] % (10**9 + 7)