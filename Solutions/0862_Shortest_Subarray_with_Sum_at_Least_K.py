class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        sol = float('inf')

        queue = collections.deque([])

        sub_sum = 0

        for index, each_num in enumerate(nums):
            sub_sum += each_num

            if sub_sum >= k:
                sol = min(sol, index+1)

            while queue and sub_sum - queue[0][0] >= k:
                pre_sum, end_index = queue.popleft()

                sol = min(sol, index - end_index)

            while queue and queue[-1][0] > sub_sum:
                queue.pop()
            
            queue.append((sub_sum, index))

        return -1 if sol==float('inf') else sol