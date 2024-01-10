class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dp = [ -1 for _ in range(n + 1)]
        dp[0] = 0
        visited = set()
        times_dict = {}
        
        for u, v, w in times:
            if u in times_dict:
                times_dict[u].append((v, w))
            else:
                times_dict[u] = [(v, w)]

        print(times_dict)
        u_list = [k]
        dp[k] = 0
        while u_list:
            u = u_list.pop(0)
            visited.add(u)

            if not u in times_dict:
                continue
            
            u_next = times_dict[u]
            u_val = dp[u]
            
            for v, w in u_next:
                if v in visited:
                    if w+dp[u] < dp[v]:
                        dp[v] = w+dp[u]
                        u_list.append(v)
                else:
                    dp[v] = w+dp[u]
                    u_list.append(v)
                visited.add(v)
        if -1 in dp:
            return -1
        return max(dp)