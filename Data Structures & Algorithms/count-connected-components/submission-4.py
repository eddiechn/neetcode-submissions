class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = [False] * n
        res = 0
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        def dfs(node):
            for n in graph[node]:
                if not visit[n]:
                    visit[n] = True
                    dfs(n)


        for i in range(n):
            if visit[i] == False:
                visit[i] = True
                res += 1
                dfs(i)

        



        return res