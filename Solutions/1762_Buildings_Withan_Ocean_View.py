class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # Varialbes
        max_height = 0
        len_heights = len(heights)
        sol = []

        # Loop - each height revesered
        for index in range(len(heights)):
            height = heights[len_heights - index - 1]
            if height > max_height: # ocean visible
                # Update sol
                sol = [len_heights - index - 1] + sol # re-calculate index (reversed order)
                # Update max_height
                max_height = height
        
        # RETURN
        return sol