class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        unequal_count = 0
        unequal_letter_s1 = ""
        unequal_letter_s2 = ""
        for each_s1, each_s2 in zip(s1, s2):
            if not each_s1 == each_s2:
                if unequal_count == 0:
                    unequal_letter_s1 = each_s1
                    unequal_letter_s2 = each_s2
                    unequal_count += 1
                elif unequal_count == 1:
                    if not (unequal_letter_s1 == each_s2 and unequal_letter_s2 == each_s1):
                        return False
                    unequal_count += 1
                else:
                    return False
        if unequal_count == 1:
            return False
        return True