class Solution:
    def isValid(self, s: str) -> bool:
        stack_list = []
        close_dict = {
            ")" : "(",
            "}" : "{",
            "]" : "[" 
        }

        for each_str in s:
            if each_str in ["(", "{", "["]:
                stack_list.append(each_str)
            else:
                close_str = close_dict[each_str]
                if len(stack_list) == 0:
                    return False
                if stack_list[-1] == close_str:
                    stack_list.pop()
                else:
                    return False
        if len(stack_list) == 0:
            return True
        else:
            return False