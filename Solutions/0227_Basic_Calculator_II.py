class Solution:
    def calculate(self, s: str) -> int:
        add_sub_list = []

        str_num = ""
        add_sub_set, mul_div_set = {"+", "-"}, {"*", "/"}
        for each_s in s + "=":
            if each_s == " ":
                continue
            
            if each_s in add_sub_set or each_s in mul_div_set:
                if add_sub_list and add_sub_list[-1] in mul_div_set:
                    last_sign = add_sub_list.pop()
                    if last_sign == "*":
                        add_sub_list[-1] = int(add_sub_list[-1] * int(str_num))
                    else:
                        add_sub_list[-1] = int(add_sub_list[-1] / int(str_num))
                    add_sub_list.append(each_s)
                else:
                    add_sub_list += [int(str_num), each_s]
                str_num = ""
            elif each_s == "=":
                if add_sub_list and add_sub_list[-1] in mul_div_set:
                    last_sign = add_sub_list.pop()
                    if last_sign == "*":
                        add_sub_list[-1] = int(add_sub_list[-1] * int(str_num))
                    else:
                        add_sub_list[-1] = int(add_sub_list[-1] / int(str_num))
                else:
                    add_sub_list += [int(str_num)]
            else:
                str_num += each_s
        sol = add_sub_list[0]
        index = 1
        while index < len(add_sub_list) - 1:
            if add_sub_list[index] == "+":
                index += 1
                sol += add_sub_list[index]
            elif add_sub_list[index] == "-":
                index += 1
                sol -= add_sub_list[index]
            index += 1
        return sol