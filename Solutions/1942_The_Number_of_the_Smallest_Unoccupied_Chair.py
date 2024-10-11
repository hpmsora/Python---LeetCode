class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Get targetFriend times range
        target_start, _ = times[targetFriend]

        # Get sorted times
        times_sorted = sorted(times)

        # Declare p list
        p_list = []

        # Loop - sorted time line
        for start_time, end_time in times_sorted:
            # Check valid target time
            if start_time < target_start:
                for index, each_p in enumerate(p_list):
                    if each_p <= start_time:
                        p_list[index] = end_time
                        break
                    if index == len(p_list) - 1:
                        p_list.append(end_time)
                        break
                if not p_list:
                    p_list.append(end_time)
            # Stop when target time here
            elif start_time == target_start:
                for index, each_p_list in enumerate(p_list):
                    if each_p_list <= target_start:
                        return index
                return len(p_list)
        