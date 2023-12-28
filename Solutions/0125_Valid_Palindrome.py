class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_list = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0','1','2','3','4','5','6','7','8','9'])
        len_s = len(s)
        count = len_s - 1
        for index in range(len_s):
            each_s = s[index].lower()
            if each_s in char_list:
                while True:
                    each_s_rev = s[count].lower()
                    print(each_s_rev)
                    if index == count:
                        return True
                    if each_s_rev in char_list:
                        if each_s_rev == each_s:
                            count -= 1
                            break
                        else:
                            return False
                    else:
                        count -= 1
                if index == count:
                    return True
            else:
                if index == count:
                    return True