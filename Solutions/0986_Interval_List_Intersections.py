class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        index_2 = 0

        sol = []

        for start, end in firstList:
            while index_2 < len(secondList) and secondList[index_2][1] < start:
                index_2 += 1
            if not index_2 < len(secondList):
                break
            

            # B Start < A Start
            if secondList[index_2][0] < start:
                # B Start < A Start < B End < A End
                if secondList[index_2][1] >= start and secondList[index_2][1] <= end:
                    sol.append([start, secondList[index_2][1]])
                    index_2 += 1
                # B Start < A Start < A End < B End
                elif secondList[index_2][1] > end:
                    sol.append([start, end])
                    continue

            # A Start < B Start
            # second index stretch
            while index_2 < len(secondList) and start > secondList[index_2][1]:
                index_2 += 1
            
            # A Start < B Start
            while index_2 < len(secondList) and secondList[index_2][0] <= end:
                # A Start < B Start < B End < A End
                if secondList[index_2][1] <= end:
                    sol.append(secondList[index_2])
                # A Start < B Start < A End < B End
                else:
                    sol.append([secondList[index_2][0], end])
                    break
                index_2 += 1

        return sol