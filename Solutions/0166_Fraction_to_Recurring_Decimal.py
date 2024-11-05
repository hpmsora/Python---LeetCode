class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sol = ""
        if numerator == 0:
            return "0"
        isNegative = False
        if numerator < 0:
            isNegative = True
            numerator *= -1
        if denominator < 0:
            isNegative = not isNegative
            denominator *= -1
        if isNegative:
            sol = "-" + sol
        if numerator >= denominator:
            sol = sol + str(numerator//denominator)
            if numerator%denominator == 0:
                return sol
            else:
                sol = sol + "."
            numerator = numerator % denominator
        else:
            sol = sol + "0."
        
        # key: numerator value: index
        seen_mode = {}
        repeat_str = ""
        numerator *= 10

        deci_list = []
        index = 0
        
        while not numerator == 0:
            seen_mode[numerator] = index
            if numerator < denominator:
                numerator *= 10
                deci_list.append("0")
                index += 1
                continue
            if numerator % denominator == 0:
                deci_list.append(str(numerator//denominator))
                return sol + ''.join(deci_list)
            else:
                deci_list.append(str(numerator//denominator))
                numerator = numerator%denominator * 10
                if numerator in seen_mode:
                    seen_index = seen_mode[numerator]
                    return sol + ''.join(deci_list[:seen_index]) + "(" + ''.join(deci_list[seen_index:]) + ")"
            index += 1
        print(sol + ''.join(deci_list))