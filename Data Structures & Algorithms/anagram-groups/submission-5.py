class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}

        for s in strs:
            count = [0] * 26 # key
            for i in range(len(s)):
                count[ord(s[i]) - ord('a')] += 1

            if tuple(count) not in res:
                res[tuple(count)] = []

            res[tuple(count)].append(s)
        
        return list(res.values())
            
        


        