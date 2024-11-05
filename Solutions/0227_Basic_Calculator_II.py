class Solution:
    def calculate(self, s: str) -> int:
        # Declare constants
        mul_div_set = {"*", "/"}
        add_sub_set = {"+", "-"}

        # Declare new list removed mul/div
        new_s_list = []

        # Declare new num string
        num = ""

        # 1. Calculate mul/div
        # Loop - string s to each letter
        for each_s in s + "=":
            # Skip space
            if each_s == " ":
                continue
            
            # Split and calculation
            if each_s in mul_div_set or each_s in add_sub_set or each_s == "=": # Operation
                # String(num) -> int(num)
                num = int(num)
                if new_s_list and (new_s_list[-1] in mul_div_set or each_s == "="):
                    if new_s_list[-1] == "*":
                        new_s_list[-2] *= num
                    elif new_s_list[-1] == "/":
                        new_s_list[-2] = int(new_s_list[-2] / num)
                    else:
                        new_s_list += [num, each_s]
                    new_s_list[-1] = each_s
                else:
                    new_s_list += [num, each_s]
                num = ""
            else: # Number
                num += each_s

        # 2. Calculate add/sub
        # Declare solution variable
        sol = new_s_list[0]

        # Loop - each mul/div removed list
        index = 1
        while index < len(new_s_list)-2:
            # Get the indexed number
            each_new_s_list = new_s_list[index]

            if each_new_s_list == "+": # Addition
                sol += new_s_list[index+1]
            else: # Substraction
                sol -= new_s_list[index+1]

            index += 2
        
        # RETURN - sol
        return sol