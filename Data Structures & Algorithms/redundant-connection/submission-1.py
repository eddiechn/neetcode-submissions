class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visit = [False] * (len(edges) + 1)
        cycle = set()
        cycleStart = -1


        def dfs(node, par):
            nonlocal cycleStart
            if visit[node]:
                cycleStart = node
                return True

            visit[node] = True
            for n in graph[node]:
                if n == par:
                    continue
                
                if dfs(n, node):
                    if cycleStart != -1:
                        cycle.add(node)

                    if node == cycleStart:
                        cycleStart = -1


                    return True


            return False


        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]


        return []
