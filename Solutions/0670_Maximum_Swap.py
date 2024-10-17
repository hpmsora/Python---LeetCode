class Solution:
    def maximumSwap(self, num: int) -> int:
        # Declare number list
        num_list = []

        # Data type [(number, index), ...]
        for index, each_num_str in enumerate(str(num)):
            num_list.append((each_num_str, index))

        # Loop - each number
        for num_set in num_list:
            num, index = num_set

            if not num == 9: # Skip if num is 9
                if index == len(num_list) - 1:
                    break
                else: # Else number
                    # Find largest rest of number
                    max_num_2, index_2 = max(num_list[index+1:])
                    # Check if number is swappable
                    if max_num_2 > num:
                        # Swap
                        num_list[index] = (max_num_2, index_2)
                        num_list[index_2] = (num, index)
                        break
        
        # Combine the number to string
        sol = ""
        for num, _ in num_list:
            sol += num
        
        # RETURN - string to number
        return int(sol)