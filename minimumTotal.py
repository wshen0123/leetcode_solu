from copy import deepcopy

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle:
            return None
        
        dp = deepcopy(triangle)
        print(dp)
        
        for i in range(1, len(triangle)):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][-1] = dp[i-1][-1] + triangle[i][-1]
            for j in range(1, len(triangle[i]) - 1):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        
        return min(dp[-1])

    
if __name__ == "__main__":
    solu = Solution()
    print(solu.minimumTotal([[1],[2,3]]))
