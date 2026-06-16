class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key not in anas:
                anas[key] = []
            anas[key].append(s)

        return list(anas.values())


        