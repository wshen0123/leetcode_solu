class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        rev_b = 0
        for i in range(32):
            rev_b |= (((n & 1<<i) >>i) <<(31-i))
        return rev_b
