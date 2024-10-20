class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        if expression == 't':
            return True
        elif expression == 'f':
            return False

        logic = expression[0]
        if logic == "&":
            par = 1
            index = 1
            new_expr = ""
            while not par == 0:
                next_str = expression[index]
                if next_str == "(":
                    if new_expr:
                        par += 1
                        new_expr += expression[index]
                    elif not par == 1:
                        par += 1
                        new_expr += expression[index]
                elif next_str == ")":
                    par -= 1
                    if par == 0:
                        temp_sol = self.parseBoolExpr(new_expr)
                        if not temp_sol:
                            return False
                        else:
                            new_expr = ""
                    else:
                        new_expr += expression[index]
                elif next_str == ",":
                    if par == 1:
                        temp_sol = self.parseBoolExpr(new_expr)
                        if not temp_sol:
                            return False
                        else:
                            new_expr = ""
                    else:
                        new_expr += expression[index]
                else:
                    new_expr += expression[index]
                index += 1
            return True
        elif logic == "|":
            par = 1
            index = 1
            new_expr = ""
            while not par == 0:
                next_str = expression[index]
                if next_str == "(":
                    if new_expr:
                        par += 1
                        new_expr += expression[index]
                    elif not par == 1:
                        par += 1
                        new_expr += expression[index]
                elif next_str == ")":
                    par -= 1
                    if par == 0:
                        temp_sol = self.parseBoolExpr(new_expr)
                        if temp_sol:
                            return True
                        else:
                            new_expr = ""
                    else:
                        new_expr += expression[index]
                elif next_str == ",":
                    if par == 1:
                        temp_sol = self.parseBoolExpr(new_expr)
                        if temp_sol:
                            return True
                        else:
                            new_expr = ""
                    else:
                        new_expr += expression[index]
                else:
                    new_expr += expression[index]
                index += 1
            return False
        elif logic == "!":
            par = 1
            index = 1
            new_expr = ""
            while not par == 0:
                next_str = expression[index]
                if next_str == "(":
                    par += 1
                    if not par == 2:
                        new_expr += expression[index]
                elif next_str == ")":
                    par -= 1
                    if par == 1:
                        temp_sol = self.parseBoolExpr(new_expr)
                        return not temp_sol
                    else:
                        new_expr += expression[index]
                else:
                    new_expr += expression[index]
                index += 1