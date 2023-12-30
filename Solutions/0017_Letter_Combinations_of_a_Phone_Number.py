class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        sol = []

        num_dict = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }

        def backtrack(_sol, _digits):
            if not _digits:
                if not _sol == "":
                    sol.append(_sol)
            else:
                digit = _digits[0]
                for letter in num_dict[digit]:
                    backtrack(_sol + letter, _digits[1:])
        backtrack("", digits)
        return sol
