class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # 1. Find max binary length
        max_num = max(nums)

        max_binary_digit = len(bin(max_num)[2:])
        k_binary = bin(k)[2:]
        k_binary_digit = len(k_binary)

        # Special Case
        if k_binary_digit > max_binary_digit:
            return -1

        # 2. Construct the initial variables
        left = 0
        right = 0
        # or_bit_comb list = [0 or 1]
        or_bit_comb = ["0" for _ in range(max_binary_digit)]
        # or_bit_comb_dict = key: index, value: 1's
        or_bit_comb_dict = {}
        # Solution variable
        min_len = float('inf')

        # 3. Sliding Windows
        while right < len(nums):
            # 3.1 Get right number
            right_num = nums[right]
            right_num_binary = bin(right_num)[2:]
            right_num_binary_digit = len(right_num_binary)
            digit_diff = max_binary_digit - right_num_binary_digit
            # 0000, 000 => 2 -> 3

            # 3.2 Update or_bit_comb
            for index, each_binary in enumerate(right_num_binary[::-1]):
                index = right_num_binary_digit - index - 1 + digit_diff
                # Update or_bit_comb
                if each_binary == "1":
                    or_bit_comb[index] = "1"
                    # Update or_bit_comb_dict
                    if index in or_bit_comb_dict:
                        or_bit_comb_dict[index] += 1
                    else:
                        or_bit_comb_dict[index] = 1

            # 3.3 Value check
            or_bit_comb_val = int(''.join(or_bit_comb), 2)
            while int(''.join(or_bit_comb), 2) >= k:
                # Update the solution
                min_len = min(min_len, right - left + 1)
                # check most left one removed
                left_num = nums[left]
                left_num_binary = bin(left_num)[2:]
                left_num_binary_digit = len(left_num_binary)
                digit_diff = max_binary_digit - left_num_binary_digit

                # Update or_bit_comb
                for index, each_binary in enumerate(left_num_binary[::-1]):
                    index = left_num_binary_digit - index - 1 + digit_diff
                    # Update or_bit_comb
                    if each_binary == "1":
                        or_bit_comb_dict[index] -= 1
                        if or_bit_comb_dict[index] == 0:
                            or_bit_comb[index] = "0"

                if int(''.join(or_bit_comb), 2) < k:
                    # Update or_bit_comb
                    for index, each_binary in enumerate(left_num_binary[::-1]):
                        index = left_num_binary_digit - index - 1 + digit_diff
                        # Update or_bit_comb
                        if each_binary == "1":
                            or_bit_comb[index] = "1"
                            # Update or_bit_comb_dict
                            if index in or_bit_comb_dict:
                                or_bit_comb_dict[index] += 1
                            else:
                                or_bit_comb_dict[index] = 1
                    break
                if left == right:
                    break
                left += 1

            # right update
            right += 1

        # 4. RETURN
        if min_len == float('inf'):
            return -1
        else:
            return min_len