class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits.sort()

        sol = []
        sol_set = set()

        for index_1, number_1 in enumerate(digits):
            if number_1 == 0:
                continue
            for index_2, number_2 in enumerate(digits):
                if index_1 == index_2:
                    continue
                for index_3, number_3 in enumerate(digits):
                    if number_3 % 2 == 1 or index_3 == index_1 or index_3 == index_2:
                        continue
                    new_num = number_1*100 + number_2 * 10 + number_3
                    if not new_num in sol_set:
                        sol.append(new_num)
                        sol_set.add(new_num)
        return sol