class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [[] for i in range(len(nums) + 1)]
        count = {}

        # counting array num:count
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        # bucket sort
        for num, cnt in count.items():
            freq[cnt].append(num)


        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            


        