class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1


        res = 0
        freq = [[] for n in range(len(nums) + 1)] 
        print(count)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for f in reversed(freq):
            if k == 0:
                return res
            for n in f:
                res.append(n)
                k -= 1




        