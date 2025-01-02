class Solution:
    def calculate(self, s: str) -> int:
        m_d = set(["*", "/"])
        p_m = set(["+", "-"])

        stack = []

        nums_str = ""
        for each_s in s:
            if each_s == " ":
                continue
            if each_s in m_d or each_s in p_m:
                nums = int(nums_str)
                if stack and stack[-1] in m_d:
                    if stack[-1] == "*":
                        stack.pop()
                        stack[-1] = stack[-1] * nums
                    else:
                        stack.pop()
                        stack[-1] = int(stack[-1] / nums)
                else:
                    stack.append(nums)
                stack.append(each_s)
                nums_str = ""
            else:
                nums_str += each_s
        if stack:
            if stack[-1] == "*":
                stack.pop()
                stack[-1] = stack[-1] * int(nums_str)
            elif stack[-1] == "/":
                stack.pop()
                stack[-1] = int(stack[-1] / int(nums_str))
            else:
                stack.append(int(nums_str))
        else:
            stack.append(int(nums_str))
        sol = stack[0]
        index = 1
        while index < len(stack):
            sign = stack[index]
            index += 1
            if sign == "+":
                sol += stack[index]
            else:
                sol -= stack[index]
            index += 1
        return sol