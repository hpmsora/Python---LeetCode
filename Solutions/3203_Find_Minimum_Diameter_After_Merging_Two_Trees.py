class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def diameter(edges):
            n=len(edges)+1
            deg=[0]*n
            adj=[[] for _ in range(n)]
            for v, w in edges:
                adj[v].append(w)
                adj[w].append(v)
                deg[v]+=1
                deg[w]+=1
            q=deque()
            for i, d in enumerate(deg):
                if d==1:
                    q.append(i)
            level, left=0, n
            while left>2:
                qz=len(q)
                left-=qz
                for i in range(qz):
                    v=q.popleft()
                    for w in adj[v]:
                        deg[w]-=1
                        if deg[w]==1:
                            q.append(w)
                level+=1
            return 2*level+1 if left==2 else 2*level

        d1=diameter(edges1)
        d2=diameter(edges2)
        return max(d1, d2, (d1+1)//2+(d2+1)//2+1)