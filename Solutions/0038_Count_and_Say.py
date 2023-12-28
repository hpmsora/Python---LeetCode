class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        n_str = "1"
        for index in range(1, n):
            temp_num = n_str[0]
            temp_count = 1
            ans = ""
            for n_index in range(1, len(n_str)):
                if temp_num == n_str[n_index]:
                    temp_count += 1
                else:
                    ans = ans + str(temp_count) + str(temp_num)
                    temp_num = n_str[n_index]
                    temp_count = 1
            ans = ans + str(temp_count) + str(temp_num)
            n_str = ans
        return n_str
