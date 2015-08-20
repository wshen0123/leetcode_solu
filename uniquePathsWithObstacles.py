class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0] *n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1 - obstacleGrid[0][0]
                    continue
                
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i - 1 >= 0:
                        fromUp = dp[i-1][j]
                    else:
                        fromUp = 0
                    if j - 1 >= 0:
                        fromLeft = dp[i][j-1]
                    else:
                        fromLeft = 0
                    dp[i][j] = fromUp + fromLeft

        print(dp)
        
        return dp[-1][-1]

if __name__ == "__main__":
    solu = Solution()
    print(solu.uniquePathsWithObstacles([[0,0]]))
