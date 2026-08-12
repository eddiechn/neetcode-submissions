class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## buckets
        """
        list -> count: elements
        sort down by count. get elemnts until k
        """ 
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        freq = [[] for n in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for f in reversed(freq):
            if k == 0:
                return res
            for n in f:
                res.append(n)
                k -= 1


        
        