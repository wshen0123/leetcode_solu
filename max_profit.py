class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit_2(self, prices):
        L = len(prices)
        if L < 2:
            return 0
        
        dp_f = [0] * L
        dp_b = [0] * L
        min_val = prices[0]
        for i in range(1, L):
            min_val = min(min_val, prices[i])
            dp_f[i] = max(dp_f[i-1], prices[i] - min_val)
        
        max_val = prices[-1]
        for i in range(L-2, -1, -1):
            max_val = max(max_val, prices[i])
            dp_b[i] = max(dp_b[i+1], max_val - prices[i])
        
        max_profit = 0
        for i in range(L):
            max_profit = max(max_profit, dp_f[i] + dp_b[i])
        
        return max_profit

    def maxProfit_inf(self, prices):
        profit = 0
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            if diff > 0:
                profit += diff
        return profit

    def maxProfit(self, k, prices):
        L = len(prices)
        if L < 2:
            return 0
        
        if k >= L / 2:
            return self.maxProfit_inf(prices)
        
        dp = [[0] * L for i in range(k+1)]
        
        for i in range(1, k+1):
            tmp_max = dp[i-1][0] - prices[0]
            for j in range(1, L):
                tmp_max = max(tmp_max, dp[i-1][j-1] - prices[j])
                dp[i][j] = max(dp[i][j-1], tmp_max + prices[j])
        
        return dp[-1][-1]

if __name__ == "__main__":
    prices = [2,1,2,0,1]
    solu = Solution()
    print(solu.maxProfit(2, prices))