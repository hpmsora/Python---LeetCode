class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        m_d_set = set(["*", "/"])
        p_n_set = set(["+", "-"])

        num = ""

        for each_s in s:
            if each_s == " ":
                continue
            if each_s in m_d_set or each_s in p_n_set:
                curr_num = int(num)
                num = ""
                if stack and stack[-1] in m_d_set:
                    sign = stack.pop()
                    if sign == "*":
                        stack.append(stack.pop() * curr_num)
                    else:
                        stack.append(int(stack.pop() / curr_num))
                else:
                    stack.append(curr_num)

                stack.append(each_s)
            else:
                num += each_s
        if not stack:
            stack.append(int(num))
        elif stack[-1] in m_d_set:
            sign = stack.pop()
            if sign == "*":
                stack.append(stack.pop() * int(num))
            else:
                stack.append(int(stack.pop() / int(num)))
        else:
            stack.append(int(num))

        index = 1
        sol = stack[0]
        while index < len(stack):
            curr = stack[index]
            index += 1
            if curr == "+":
                sol += stack[index]
            else:
                sol -= stack[index]
            index += 1
        return sol