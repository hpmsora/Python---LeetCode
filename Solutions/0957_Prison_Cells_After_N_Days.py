class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        n_prison = 8
        
        # Day 1 first, last cell rule
        new_cells = [0 for _ in range(n_prison)]
        key = ""
        for index in range(1, n_prison-1):
            cell_f = cells[index - 1]
            cell_b = cells[index + 1]
            if cell_f == cell_b:
                new_cells[index] = 1
                key += str(index)
        cells = new_cells
        
        # Loop
        order_dict = {}
        order_dict[key] = 0
        order_dict_index = 1
        n = n-1
        while n > 0:
            new_cells = [0 for _ in range(n_prison)]
            key = ""
            for index in range(1, n_prison-1):
                cell_f = cells[index - 1]
                cell_b = cells[index + 1]
                if cell_f == cell_b:
                    new_cells[index] = 1
                    key += str(index)
            cells = new_cells
            str_cells = str(cells)
            
            if key in order_dict:
                d_index = order_dict[key]
                roop_size = order_dict_index - d_index
                n = (n-1)%roop_size
                key = list(order_dict.keys())[d_index + n]
                new_cells = [0 for _ in range(n_prison)]
                for each_key in key:
                    new_cells[int(each_key)] = 1
                return new_cells
            else:
                order_dict[key] = order_dict_index
                order_dict_index += 1
            
            n-=1
        
        return cells