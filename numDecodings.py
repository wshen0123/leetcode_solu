class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        L = len(s)
        if L == 0:
            return 0
        
        
        if s[0] == "0":
            return 0
        
        if L == 1:
            return 1
        
        dp = [0] * (L + 2)
        dp[-1] = 1
        dp[-2] = 1
        
        dp[0] = 1

        for i in range(1, L):
            if s[i] != "0":
                dp[i] += dp[i-1]
                val = int(s[i-1] + s[i])
                if val >= 11 and val <= 26:
                    dp[i] += dp[i-2]
            else:
                val = int(s[i-1] + s[i])
                if val >= 1 and val <= 26:
                    dp[i] += dp[i-2]
                else:
                    return 0
        
        print(dp)
        return dp[L-1]
    
if __name__ == "__main__":
    solu = Solution()
    s = "123"
    print(solu.numDecodings(s))