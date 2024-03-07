class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        smallest_index = -1
        smallest_num = float('inf')

        while k > 0:
            index = 0

            smallest_num = float('inf')
            while index < len(matrix):
                if len(matrix[index]) == 0:
                    index += 1
                    continue
                if smallest_num >= matrix[index][0]:
                    smallest_index = index
                    smallest_num = matrix[index][0]
                index += 1
            matrix[smallest_index].pop(0)
            k -= 1
        return smallest_num