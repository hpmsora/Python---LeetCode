class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        visited = set()
        for u_i, v_i in edges:
            if u_i in visited:
                return u_i
            else:
                visited.add(u_i)
            if v_i in visited:
                return v_i
            else:
                visited.add(v_i)