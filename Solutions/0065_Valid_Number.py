class Solution:
    def isNumber(self, s: str) -> bool:
        num_set = { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" }
        p_n_set = {"-", "+"}

        # 0. All letter lower
        s = s.lower()

        # 1. Exponent check
        s_list = s.split("e")
        if len(s_list) > 2:
            return False
        
        # 2. Number Check
        for index in range(len(s_list)):
            each_s_list = s_list[index]
            # 2.1 Sign Check
            if each_s_list and each_s_list[0] in p_n_set:
                each_s_list = each_s_list[1:]
                if len(each_s_list) == 0 or each_s_list[0] in p_n_set:
                    return False

            # 2.2 Emtpy check
            if not each_s_list:
                return False
            
            # 2.3 Dot split
            each_s_list_dot_split = each_s_list.split(".")
            if index == 1 and len(each_s_list_dot_split) == 2:
                return False
            if len(each_s_list_dot_split) > 2:
                return False
            elif len(each_s_list_dot_split) == 2:
                if (not each_s_list_dot_split[0]) and (not each_s_list_dot_split[1]):
                    print("AA")
                    return False
            
            # 2.4 Only number check
            for index, each_each_s_list_dot_split in enumerate(each_s_list_dot_split):
                for each_letter in each_each_s_list_dot_split:
                    if not each_letter in num_set:
                        return False
        return True