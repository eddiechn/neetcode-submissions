class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        freq: numbers
        """

        buckets = [[] for n in range(len(nums) + 1)]
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1


        for n, c in freq.items():
            buckets[c].append(n)

        res = []

        for f in reversed(buckets):
            if k == 0:
                return res

            for n in f:
                res.append(n)
                k -= 1


        return res


        







        