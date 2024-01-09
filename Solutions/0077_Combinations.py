class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []
        def helper(_list, k, _prev, _sol):
            if k == 0:
                _sol.append(_prev)
                return

            sol = []
            for index in range(len(_list) - k + 1):
                num = _list[index]
                new_prev = _prev[:]
                new_prev.append(num)
                new_list = _list[index + 1:]
                helper(new_list, k - 1, new_prev, _sol)
            return
        helper([x for x in range(1, n + 1)], k, [], sol)

        return sol