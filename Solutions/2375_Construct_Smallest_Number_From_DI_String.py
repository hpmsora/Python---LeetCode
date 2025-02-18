class Solution:
    def smallestNumber(self, pattern: str) -> str:
        num_list = [x + 1 for x in range(len(pattern)+1)]

        prev_pattern = [pattern[0]]

        pattern_list = []

        for each_pattern in pattern[1:]:
            if each_pattern == "D" and prev_pattern[-1] == "I":
                pattern_list.append(prev_pattern)
                prev_pattern = [each_pattern]
            else:
                prev_pattern.append(each_pattern)
        pattern_list.append(prev_pattern)

        sol = ""

        index = 0
        for order, each_pattern_list in enumerate(pattern_list):
            prev_index = index
            if order == len(pattern_list)-1:
                index += len(each_pattern_list) + 1
            else:
                index += len(each_pattern_list)

            new_num_list = num_list[prev_index:index]
            index_2 = 0

            for each_pattern in each_pattern_list:
                if each_pattern == "I":
                    break
                index_2 += 1
            sol += ''.join(str(x) for x in new_num_list[index_2::-1])
            if not index_2 == len(each_pattern_list):
                sol += ''.join(str(x) for x in new_num_list[index_2+1:])
        return sol