class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums_dict = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        
        if not digits:
            return []
        val = nums_dict[digits[0]]
        sol = []
        for each_val in val:
            sol.append(each_val)
        
        index = 1
        while index < len(digits):
            letters = nums_dict[digits[index]]
            index += 1
            new_sol = []
            for each_letters in letters:
                for each_sol in sol:
                    new_sol.append(each_sol+each_letters)
            sol = new_sol
        return sol