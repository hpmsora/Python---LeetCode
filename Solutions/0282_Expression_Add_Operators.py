class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # 1. Find empty slots
        # 2. Calculate each statement
        
        # 1. Find empty slots
        num_list = list(num)
        index = 1
        empty_slot_index = []
        while index < len(num_list):
            num_list = num_list[:index] + [""] + num_list[index:]
            empty_slot_index.append(index)
            index += 2
            
        # 2. Calculate each statement
        def helper(_num_list, _empty_slot_index, _cal_list):
            if not _empty_slot_index:
                num_str = ''.join(_num_list)
                for each_num in num_str.replace('+',' ').replace('-',' ').replace('*',' ').split():
                    if len(each_num) > 1 and each_num[0] == "0":
                        return []
                
                if eval(num_str) == target:
                    return [''.join(_num_list)]
                else:
                    return []
            sol = []
            for each_cal_list in _cal_list:
                _num_list[_empty_slot_index[0]] = each_cal_list
                sol += helper(_num_list, _empty_slot_index[1:], _cal_list)
            return sol
        
        cal_list = ['+', '-', '*', '']
        sol = []
        
        sol = helper(num_list, empty_slot_index, cal_list)
        return sol