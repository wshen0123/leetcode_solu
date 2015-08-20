class Solution:
    # @param {integer} n
    # @return {integer}
    cache = {}
    
    def numTrees(self, n):
        def numSubTrees(n):
            if n in Solution.cache:
                return Solution.cache[n]
            if n == 0:
                return 1
            cnt = 0
            nodes_left = n - 1
            for i in range(0, nodes_left + 1):
                cnt += numSubTrees(i) * numSubTrees(nodes_left - i)
            
            Solution.cache[n] = cnt
            return cnt
            
        if n == 0:
            return 0
        
        return numSubTrees(n)
