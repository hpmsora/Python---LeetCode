class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat) # n row
        m = len(mat[0]) # n column
        
        for index_m in range(m):
            # right top
            temp_list = []
            temp_index_m = index_m
            for index_n in range(n):
                num = mat[index_n][temp_index_m]
                temp_list.append(num)
                temp_index_m += 1
                if temp_index_m == m:
                    break
            
            temp_list.sort()
            
            index = 0
            temp_index_m = index_m
            for index_n in range(n):
                mat[index_n][temp_index_m] = temp_list[index]
                temp_index_m += 1
                if temp_index_m == m:
                    break
                index += 1
                
            # left bottom
            if index_m == 0:
                for index_n_bottom in range(1, n):
                    temp_list = []
                    temp_index_n_bottom = index_n_bottom
                    
                    for index_m in range(m):
                        num = mat[temp_index_n_bottom][index_m]
                        temp_list.append(num)
                        temp_index_n_bottom += 1
                        if temp_index_n_bottom == n:
                            break
                    
                    temp_list.sort()
                    index = 0
                    temp_index_n_bottom = index_n_bottom
                    
                    for index_m in range(m):
                        mat[temp_index_n_bottom][index_m] = temp_list[index]
                        index += 1
                        temp_index_n_bottom += 1
                        if temp_index_n_bottom == n:
                            break
        return mat