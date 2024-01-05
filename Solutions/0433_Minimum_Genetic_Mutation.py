class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def isMutable(_gene_1, _gene_2):
            diff = 0
            for c_1, c_2 in zip(_gene_1, _gene_2):
                if not c_1 == c_2:
                    diff += 1
                    if diff > 1:
                        return False
            if diff == 1:
                return True
            else:
                return False
        
        def helper(_gene_1, _gene_2, _bank, n_m):
            if _gene_1 == _gene_2:
                return n_m

            sol = []
            for index in range(len(_bank)):
                each_bank = _bank[index]
                if isMutable(_gene_1, each_bank):
                    if index < len(_bank)-1:
                        sol.append(helper(each_bank, _gene_2, _bank[:index]+_bank[index + 1:], n_m + 1))
                    else:
                        sol.append(helper(each_bank, _gene_2, _bank[:index], n_m + 1))
            
            if len(sol) == 0:
                nonlocal size_bank
                return size_bank + 1
            else:
                return min(sol)
        size_bank = len(bank)

        sol = helper(startGene, endGene, bank, 0)
        if sol == size_bank + 1:
            return -1
        return sol