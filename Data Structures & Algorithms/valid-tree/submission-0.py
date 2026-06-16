class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        # just detect the cycle
        visited = set()

        # construct graph
        graph = defaultdict(list)
        for i, o in edges:
            graph[i].append(o)
            graph[o].append(i)


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
