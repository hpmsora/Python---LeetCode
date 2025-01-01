class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = collections.deque()

        for each_s in s:
            if each_s == "(":
                stack.append("(")
            elif each_s == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(")")
        return len(stack)