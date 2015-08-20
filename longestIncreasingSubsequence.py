class Solution:
    def longestIncreasingSubsequence(self, nums):
        N = len(nums)
        L = [1] * N
        longest = 0
        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i] and L[j] + 1 > L[i]:
                    L[i] = L[j] + 1
            if L[i] > longest:
                longest = L[i]
        print(L)
        return longest
