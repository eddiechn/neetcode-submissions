class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        dict: key: []

        key = sorted(str)

        return dict.values()
     """
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            key = str(count)

            res[key].append(s)
            
        return list(res.values())

        