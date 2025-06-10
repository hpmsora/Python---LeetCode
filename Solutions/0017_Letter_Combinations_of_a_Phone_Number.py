class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        
        sol = []
        
        for each_digits in digits:
            letters = num_dict[each_digits]
            
            new_sol = []
            for each_letter in letters:
                if not sol:
                    new_sol.append(each_letter)
                else:
                    for each_sol in sol:
                        new_sol.append(each_sol + each_letter)
            sol = new_sol
            
        return sol