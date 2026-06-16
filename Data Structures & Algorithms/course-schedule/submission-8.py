class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        build a graph b -> a
        start with nodes with no prereq,
        remove connection to courses 
        if connection == 0: add to queue
        if res == numCourses return True else False
        """

        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1

        q = deque()

        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        res = 0

        while q:
 
            node = q.popleft()
            res += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
        
                    q.append(nei)


        return True if res == numCourses else False