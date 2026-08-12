class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        match = {}
        for s in strs:
            count = [0] * 26
            for t in s:
                count[ord(t) - ord('a')] += 1

            key = tuple(count)
            if key not in match:
                match[key] = []

            match[key].append(s)


        return list(match.values())


        