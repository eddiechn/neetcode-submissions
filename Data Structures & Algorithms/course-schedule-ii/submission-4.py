class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        res = []
        q = deque()


        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        while q:
            node = q.popleft()
            res.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(res) != numCourses:
            return []
        return res

        