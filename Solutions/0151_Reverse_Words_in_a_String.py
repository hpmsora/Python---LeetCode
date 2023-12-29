class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")

        sol = ""
        for each_s_list in s_list:
            if each_s_list:
                sol = each_s_list + " " + sol
        return sol[:-1]