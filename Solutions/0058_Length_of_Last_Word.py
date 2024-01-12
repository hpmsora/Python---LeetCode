class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split(" ")

        for each_list in reversed(s_list):
            if not each_list == "":
                return (len(each_list))