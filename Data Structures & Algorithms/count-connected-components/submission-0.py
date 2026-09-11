class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        res = 0

        def dfs(node,par):
            if node in visit:
                return 0 
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue 
                dfs(nei,node)
            return 1 
            
        for i in range(n):
            res+= dfs(i,-1)
        return res
