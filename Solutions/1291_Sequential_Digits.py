class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        possible_num_list = []
        for n_digits in range(2,10):
            for first_digit in range(1,10-n_digits + 1):
                temp_num = []
                for num in range(first_digit,first_digit+n_digits):
                    temp_num.append(str(num))
                possible_num_list.append(int(''.join(temp_num)))
        sol = []
        for possible_num in possible_num_list:
            if low <= possible_num and possible_num <= high:
                sol.append(possible_num)
        return sol