class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        if not s:
            return False

        wordDictLens = list(map(len, list(wordDict)))
        min_len = min(wordDictLens)
        max_len = max(wordDictLens)

        s_len = len(s)
        dp_len = s_len + 1
        
        dp = [False] * dp_len
        dp[0] = True

        for i in range(1, dp_len):
            for l in range(min_len, max_len + 1):
                if i - l < 0:
                    continue
                else:
                    if s[i-l:i] in wordDict and dp[i-l]:
                        dp[i] = True
                        break

        return dp[-1]

if __name__ == "__main__":
    solu = Solution()
    s = "leetcode"
    wd = set(["leet", "code"])

    print(solu.wordBreak(s, wd))
