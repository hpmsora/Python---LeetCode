class Solution:
    def minEnd(self, n: int, x: int) -> int:
        if n == 1:
            return x
        x_binary = bin(x)[2:]
        n -= 1
        
        x_zeros = 0
        for each_x_binary in x_binary:
            if each_x_binary == "0":
                x_zeros += 1

        x_combination = 2**x_zeros
        prefix = n // x_combination
        suffix = n % x_combination

        prefix_start = len(x_binary)
        prefix_binary =  bin(prefix)[2:]
        prefix_num = 0
        for index, each_prefix_binary in enumerate(prefix_binary[::-1]):
            if each_prefix_binary == "1":
                prefix_num += 2**(prefix_start + index)

        suffix_binary = bin(suffix)[2:]
        suffix_num = 0

        suffix_binary_index = 1
        for index, each_x_binary in enumerate(x_binary[::-1]):
            if each_x_binary == "1":
                suffix_num += 2**index
            else:
                if len(suffix_binary) - suffix_binary_index >= 0:
                    if suffix_binary[len(suffix_binary) - suffix_binary_index] == "1":
                        suffix_num += 2**index
                    suffix_binary_index += 1
        return prefix_num + suffix_num