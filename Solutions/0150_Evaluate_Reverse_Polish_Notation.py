class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        new_list = []
        operation_set = {'+', '-', '*', '/'}

        for token in tokens:
            if token in operation_set:
                num_2 = new_list.pop()
                num_1 = new_list.pop()
                if token == '+':
                    new_list.append(num_1 + num_2)
                elif token == '-':
                    new_list.append(num_1 - num_2)
                elif token == '*':
                    new_list.append(num_1 * num_2)
                elif token == '/':
                    new_list.append(int(num_1 / num_2))
            else:
                new_list.append(int(token))
        return new_list.pop()