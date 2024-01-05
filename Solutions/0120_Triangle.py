class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        for index in range(1, len(triangle)):
            row = triangle[index]
            for index_2 in range(len(row)):
                if index_2 == 0:
                    row[index_2] += triangle[index-1][index_2]
                elif index_2 == len(row) - 1:
                    row[index_2] += triangle[index-1][index_2-1]
                else:
                    row[index_2] += min(triangle[index-1][index_2], triangle[index-1][index_2-1])
        return min(row)
