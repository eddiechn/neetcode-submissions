class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        res = []

        while k > 0:
            a = heapq.heappop(nums)
            res.append(a)
            k -= 1
        
        return -(res[-1])


        