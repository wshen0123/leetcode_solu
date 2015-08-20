class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        m1 = m2 = None
        c1 = c2 = 0
        
        for n in nums:
            if n == m1:
                c1 += 1
            elif n == m2:
                c2 += 1
            elif c1 == 0:
                m1, c1 = n, 1
            elif c2 == 0:
                m2, c2 = n, 1
            else:
                c1 -= 1
                c2 -= 1
        
        L = len(nums)
        return [m for m in (m1,m2) if nums.count(m) > (L/3)]