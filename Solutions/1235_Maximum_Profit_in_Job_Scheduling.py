class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        tup_slot_list = []
        dp_size = 0
        dp = {
            0 : 0
        }
        for s_t, e_t, pro in zip(startTime, endTime, profit):
            tup_slot_list.append((s_t, e_t, pro))
            if dp_size < e_t:
                dp_size = e_t
            dp[s_t] = 0
            dp[e_t] = 0
        tup_slot_list.sort()

        max_profit = 0
        prev_s_t = 0
        prev_max = 0
        valid_set = [0]
        for s_t, e_t, pro in tup_slot_list:
            max_prev = 0
            dp_max = 0
            cut_index = 0
            
            for each_valid_set in valid_set:
                if each_valid_set < prev_s_t:
                    cut_index += 1
                elif each_valid_set <= s_t:
                    if dp[each_valid_set] > dp_max:
                        dp_max = dp[each_valid_set]
                else:
                    break
            valid_set = valid_set[cut_index:]

            dp_max = max(prev_max, dp_max)
            prev_max = dp_max
            val = dp_max + pro

            dp[e_t] = max(dp[e_t], val)
            prev_s_t = s_t

            valid_set.append(e_t)
            valid_set.sort()

            if max_profit < val:
                max_profit = val
        return max_profit