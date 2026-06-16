class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        res = []
        indegree = [0] * numCourses
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1


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

        res.reverse()
        return res
