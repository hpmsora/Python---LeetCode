class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        cons_color = None
        cons_time_list = []
        total_time = 0
        for index in range(len(colors)):
            each_colors = colors[index]
            each_time = neededTime[index]
            if each_colors == cons_color:
                cons_time_list.append(neededTime[index])
            else:
                if len(cons_time_list) > 1:
                    total_time += sum(cons_time_list) - max(cons_time_list)
                cons_time_list = [each_time]
                cons_color = each_colors
        if len(cons_time_list) > 1:
            total_time += sum(cons_time_list) - max(cons_time_list)
        return total_time