class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        sol = []
        if k == 0:
            return [0] * len(code)
        elif k > 0:
            sub_sum = sum(code[1:k+1])
            sol.append(sub_sum)
            for index, each_code in enumerate(code[1:]):
                index += 1
                last_num = code[(index + k) % len(code)]
                sub_sum = sub_sum - each_code + last_num
                sol.append(sub_sum)
            return sol
        else:
            sub_sum = sum(code[k:])
            sol.append(sub_sum)
            for index, each_code in enumerate(code[:-1]):
                index += 1
                last_num = code[index + k-1]
                sub_sum = sub_sum + each_code - last_num
                sol.append(sub_sum)

            return sol