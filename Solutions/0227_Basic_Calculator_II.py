class Solution:
    def calculate(self, s: str) -> int:
        # Calculation List
        cal_list = []

        # Operation set
        opt_set = {
            "/", "*", "+", "-"
        }

        # Loop - Calculation List
        prev = ""
        for each_s in s:
            if each_s == " ": # Empty
                continue
            
            if each_s in opt_set: # Operation char
                cal_list.append(int(prev))
                cal_list.append(each_s)
                prev = ""
            else: # number char
                prev += each_s
        # Remaining num
        cal_list.append(int(prev))

        # Calculation Loop - Remove mul and div
        prev = 0
        new_cal_list = []
        index = 0
        while index < len(cal_list):
            each_cal = cal_list[index]
            if each_cal in opt_set:
                if each_cal == "/": # division
                    prev = prev // cal_list[index + 1]
                    index += 2
                elif each_cal == "*": # multiplication
                    prev = prev * cal_list[index + 1]
                    index += 2
                else:
                    new_cal_list.append(prev)
                    new_cal_list.append(each_cal)
                    prev = 0
                    index += 1
            else:
                prev = each_cal
                index += 1
        # Remaining num
        new_cal_list.append(prev)

        # Calculation Loop - Remove add and sub
        index = 0
        sol = 0
        while index < len(new_cal_list):
            each_new_cal = new_cal_list[index]
            if each_new_cal == "+": # addition
                sol += new_cal_list[index + 1]
                index += 2
            elif each_new_cal == "-": # subtraction
                sol -= new_cal_list[index + 1]
                index += 2
            else:
                sol = each_new_cal
                index += 1
        
        #RETURN
        return sol