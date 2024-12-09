class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n_speical_list = []

        prev_num = nums[0]

        for index, each_nums in enumerate(nums[1:]):

            if prev_num % 2 == each_nums % 2:
                n_speical_list.append((index, index + 1))
            prev_num = each_nums

        sol = []

        for start, end in queries:
            index = 0
            if not n_speical_list or end - start == 0:
                sol.append(True)
                continue
            
            isTrue = True
            left = 0
            right = len(n_speical_list) - 1
            while left <= right:
                mid = (left+right) // 2

                n_start, n_end = n_speical_list[mid]
                if start <= n_start and n_end <= end:
                    isTrue = False
                    sol.append(False)
                    break
                if n_end <= start:
                    left = mid + 1
                else:
                    right = mid - 1
            if isTrue:
                sol.append(True)
        return sol