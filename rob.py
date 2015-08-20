class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        N = len(nums)
        
        if N == 0:
            return 0
        elif N == 1:
            return nums[0]
        
        L = [0] * N
        L[0] = nums[0]
        L[1] = max(nums[0], nums[1])
        
        for i in range(2,N):
            L[i] = max(nums[i] + L[i-2], L[i-1])

        return max(L)
