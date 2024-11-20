class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # [(str("(" or ")"), int(index))]
        stack = []

        # str(s) -> list(s)
        s_list = list(s)

        for index, each_s in enumerate(s_list):
            # Case 1: "("
            if each_s == "(":
                stack.append(("(", index))
            # Case 2: ")"
            elif each_s == ")":
                # Case 2-1: remove "("
                if stack and stack[-1][0] == "(":
                    stack.pop()
                # Case 2-2: append ")"
                else:
                    stack.append((")", index))
        
        # str(s) remove unnecessary parenthesis
        for _, index in stack:
            s_list[index] = ""
        
        # RETURN - list(s_list) -> str(s)
        return ''.join(s_list)