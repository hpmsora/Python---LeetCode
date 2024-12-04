class Solution:
    def calculate(self, s: str) -> int:
        
        cal_list = []

        index = 0

        operators_pn = {'+', '-'} 
        operators_md = {'*', '/'}

        curr_num = ""

        while index < len(s):
            curr_letter = s[index]

            if curr_letter == " ":
                index += 1
                continue

            if curr_letter in operators_pn or curr_letter in operators_md:
                if cal_list and cal_list[-1] in operators_md:
                    curr_operator = cal_list.pop()

                    if curr_operator == "*":
                        cal_list[-1] = cal_list[-1] * int(curr_num)
                    else:
                        cal_list[-1] = cal_list[-1] // int(curr_num)
                    cal_list.append(curr_letter)
                else:
                    cal_list.append(int(curr_num))
                    cal_list.append(curr_letter)
                curr_num = ""
            else:
                curr_num += curr_letter
            index += 1
        if cal_list and cal_list[-1] == "*":
            cal_list.pop()
            cal_list[-1] = cal_list[-1] * int(curr_num)
        elif cal_list and cal_list[-1] == "/":
            cal_list.pop()
            cal_list[-1] = cal_list[-1] // int(curr_num)
        else:
            cal_list.append(int(curr_num))
        sol = 0
        curr_opreator = "+"
        for each_cal_list in cal_list:
            if each_cal_list in operators_pn:
                curr_opreator = each_cal_list
            else:
                if curr_opreator == "+":
                    sol += each_cal_list
                else:
                    sol -= each_cal_list
        return sol