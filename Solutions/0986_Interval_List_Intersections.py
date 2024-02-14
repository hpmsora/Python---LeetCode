class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        def common_interval(_interval_1, _interval_2):
            start_1, end_1 = _interval_1
            start_2, end_2 = _interval_2

            start_sol = -1
            if start_1 > start_2:
                start_sol = start_1
            else:
                start_sol = start_2

            end_sol = -2
            if end_1 < end_2:
                end_sol = end_1
            else:
                end_sol = end_2

            isRemove = False
            if end_1 >= end_2:
                isRemove = True

            if start_sol <= end_sol:
                return ([start_sol, end_sol], isRemove)
            else:
                return ([], isRemove)

        sol = []
        for each_firstList in firstList:
            if not secondList:
                break
            while secondList:
                sub_list = secondList[0]
                temp_sol, isRemove = common_interval(each_firstList, sub_list)

                if temp_sol:
                    sol.append(temp_sol)
                
                if isRemove:
                    secondList.pop(0)
                else:
                    break
        return sol