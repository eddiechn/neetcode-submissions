class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        dp[i] = True if s[0:i] can be segmented
        lookup time complexity in set is O(1) vs O(n) for a list

        Input: s = "neetcode", wordDict = ["neet","code"]
        dp[3] = True
        """
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break


        return dp[len(s)]
