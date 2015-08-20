class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        len_s = len(s)
        len_t = len(t)
        
        if len_t == 0 or len_s == 0:
            return 0
            
        dp = [[0] * len_t for i in range(len_s)] # len_s by len_t

        for i in range(len_s):
            dp[i][0] = dp[i-1][0] + (1 if s[i] == t[0] else 0)
        
        for i in range(1, len_s):
            for j in range(1, len_t):
                dp[i][j] = dp[i-1][j] + (dp[i-1][j-1] if s[i] == t[j] else 0)

        return dp[-1][-1]
        


solu = Solution()
dp = solu.numDistinct("rabbbit", "rabbit")
print(dp)
