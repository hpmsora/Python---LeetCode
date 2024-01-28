class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        sol = ['' for _ in range(max(indices) + 1)]
        
        for char, index in zip(s, indices):
            sol[index] = char
            
        return ''.join(sol)