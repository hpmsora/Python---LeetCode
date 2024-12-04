# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate_list = [index for index in range(n)]

        for index_1 in range(n):
            index_2 = 0
            while index_2 < len(candidate_list):
                curr_can = candidate_list[index_2]

                if not knows(index_1, curr_can):
                    candidate_list.pop(index_2)
                else:
                    index_2 += 1
        sol = []

        for each_candidate_list in candidate_list:
            isCandidate = True
            for index in range(n):
                if knows(each_candidate_list, index) == 1 and not index == each_candidate_list:
                    isCandidate = False
                    break
            if isCandidate:
                sol.append(each_candidate_list)
                if len(sol) > 1:
                    return -1
        if sol:
            return sol[0]
        else:
            return -1