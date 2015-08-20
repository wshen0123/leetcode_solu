import math

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        return math.factorial(m+n)/(math.factorial(m) * math.factorial(n))
