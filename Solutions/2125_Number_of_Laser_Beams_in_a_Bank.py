class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        s_list = []
        sol = 0
        for each_bank in bank:
            count = 0
            for cell in each_bank:
                if cell == "1":
                    count += 1
            if not count == 0:
                s_list.append(count)
        if len(s_list) > 1:
            for index in range(len(s_list) - 1):
                sol += s_list[index] * s_list[index + 1]
            return sol
        return 0