class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

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
            