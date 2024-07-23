class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tupNameHeight = []

        for name, height in zip(names, heights):
            tupNameHeight.append((height, name))
        
        tupNameHeight.sort(reverse=True)

        sol = []

        for _, name in tupNameHeight:
            sol.append(name)

        return sol