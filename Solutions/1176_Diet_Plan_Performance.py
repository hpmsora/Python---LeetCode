class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        index = 0
        sol = 0
        
        total_cal = sum(calories[:k])
        if total_cal < lower:
            sol -= 1
        elif total_cal > upper:
            sol += 1
        
        for index in range(1,len(calories) - k + 1):
            total_cal += (calories[index+k-1] - calories[index - 1])
            
            if total_cal < lower:
                sol -= 1
            elif total_cal > upper:
                sol += 1
        
        return sol