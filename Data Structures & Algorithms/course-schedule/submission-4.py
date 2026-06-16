class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # kahn's algorithm
        indegree = [0] * numCourses
        finish = 0
        q = deque()

        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        for n in range(numCourses):
            if indegree[n] == 0: # find courses that are not required by any other course
                q.append(n)


        while q:
            node = q.popleft()
            finish += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)


        return finish == numCourses

        