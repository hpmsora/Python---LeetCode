class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Declare task frequency dictionary
        task_freq_dict = {}

        # Loop - check all task in tasks
        for task in tasks:
            if task in task_freq_dict:
                task_freq_dict[task] += 1
            else:
                task_freq_dict[task] = 1

        task_freq_list = []
        for key, freq in task_freq_dict.items():
            task_freq_list.append([freq, key])

        task_freq_list.sort()

        min_freq, _ = task_freq_list.pop()

        sol = (min_freq - 1) * n

        for freq, _ in task_freq_list:
            sol -= min(min_freq - 1, freq)

        return len(tasks) + sol if sol >= 0 else len(tasks)