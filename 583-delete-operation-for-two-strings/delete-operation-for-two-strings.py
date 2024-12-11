class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def longestCommonSubsequence(text1, text2):
            dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

            for i in range(len(text1) - 1, -1, -1):
                for j in range(len(text2) - 1, -1, -1):
                    if text1[i] == text2[j]:
                        dp[i][j] = 1 + dp[i + 1][j + 1]
                    else:
                        dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
            
            return dp[0][0]
        
        m, n = len(word1), len(word2)
        return m + n - (2 * longestCommonSubsequence(word1, word2))