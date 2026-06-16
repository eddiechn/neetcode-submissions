class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereq = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            prereq[b].append(a)
            indegree[a] += 1


        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        res = 0
        while q:
            n = q.popleft()
            res += 1
            for nei in prereq[n]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)


        return True if res == numCourses else False

