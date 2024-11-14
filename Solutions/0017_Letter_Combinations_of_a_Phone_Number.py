class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        sol = [""]
        
        for each_digits in digits:
            new_sol = []
            for each_sol in sol:
                for each_letter in num_map[each_digits]:
                    new_sol.append(each_sol + each_letter)
            sol = new_sol
        return sol