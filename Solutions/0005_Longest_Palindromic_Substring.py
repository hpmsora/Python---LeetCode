class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPal(_s):
            return _s == _s[::-1]

        start_index = 0
        sol = s[0]

        index = 0
        while index < len(s):
            start_index = index
            for last_index in range(start_index+1, len(s) + 1):
                cur_s = s[start_index:last_index]
                if isPal(cur_s):
                    if len(sol) < (last_index - start_index):
                        sol = cur_s
                    
                    #rev_cur_s = cur_s[::-1]
                    #for start_index_2 in range(last_index + 1, len(s) + 1 - (last_index - start_index)):
                    #    if s[start_index_2:start_index_2+(last_index - start_index)] == rev_cur_s:
                    #        if isPal(s[index:start_index_2+(last_index - start_index)]):
                    #            if len(sol) < (start_index_2+(last_index - start_index) - index):
                    #                sol = s[start_index_2:start_index_2+(last_index - start_index)]
                    #index = last_index - 1
                    #continue
            index += 1
        return sol