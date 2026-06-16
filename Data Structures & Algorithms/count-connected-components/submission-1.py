class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visit = [False] * n


        def dfs(node):
            for nei in graph[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)



        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1

        return res