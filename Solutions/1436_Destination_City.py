class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start_set = set()
        end_set = set()

        for start, end in paths:
            start_set.add(start)
            end_set.add(end)
        
        for end in end_set:
            if not end in start_set:
                return end