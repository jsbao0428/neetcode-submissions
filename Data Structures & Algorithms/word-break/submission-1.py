class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        """

        dp[i] = # 前 i 個可不可以被切
        for j in range(i):
            
        """
        n = len(s)
        dp = [False] * (n + 1)
        wordDict = set(wordDict)

        # base case 
        dp[0] = True
        for i in range(n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True

        return dp[n]
                    


