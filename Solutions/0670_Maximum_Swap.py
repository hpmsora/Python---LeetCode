class Solution:
    def maximumSwap(self, num: int) -> int:
        # num list from num
        num_list = []

        # loop - get num_list
        for each_num in str(num):
            num_list.append(int(each_num))
        
        # sort the list
        num_list_sorted = sorted(num_list, reverse=True)

        # Loop - num_list and num_list_sorted compare each element
        isChange = False
        index_1, index_2 = 0, 0
        for index in range(len(num_list)):
            each_num, each_num_sorted = num_list[index], num_list_sorted[index]
            if isChange:
                if num_list_sorted[index_1] == num_list[index]:
                    index_2 = index
            if not isChange and not each_num == each_num_sorted:
                isChange = True
                index_1 = index
        
        # Swap check
        if isChange: # need swap
            # Swap the num
            temp_num = num_list[index_1]
            num_list[index_1] = num_list[index_2]
            num_list[index_2] = temp_num

            # RETURN
            return int(''.join(map(str, num_list)))
        else: # no need to swap
            #RETURN
            return num
        