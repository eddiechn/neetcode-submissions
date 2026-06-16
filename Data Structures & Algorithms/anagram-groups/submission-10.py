class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = {}
        res = []

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = str(count)
        
            if key not in group:
                group[key] = []
            group[key].append(s)

        for v in group.values():
            res.append(v)


        return res