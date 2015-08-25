class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return None
        
        l = [1] * n
        i2 = i3 = i5 = 0
        for i in range(1,n):
            v2 = l[i2] * 2
            v3 = l[i3] * 3
            v5 = l[i5] * 5
            vi = min(v2, v3, v5)
            i2 += 1 if vi == v2 else 0
            i3 += 1 if vi == v3 else 0
            i5 += 1 if vi == v5 else 0
            l[i] = vi
        
        return l[-1]
    
if __name__ == "__main__":
    solu = Solution()
    print(solu.nthUglyNumber(10))