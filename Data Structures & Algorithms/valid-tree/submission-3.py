class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        "valid tree -> no cycles, no unconnected components"


        visited = set()
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        def dfs(node, par):
            if node in visited:
                return False

            visited.add(node)
            for nei in graph[node]:
                if nei == par:
                    continue

                if not dfs(nei, node):
                    return False


            return True

        return dfs(0, -1) and len(visited) == n

        