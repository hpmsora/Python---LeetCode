class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces_set = set(spaces)

        index = 0
        sol = []

        for each_spaces in spaces:
            sol.append(s[index: each_spaces])
            index = each_spaces
        sol.append(s[index:])

        return ' '.join(sol)