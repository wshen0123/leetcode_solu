class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        left = 1
        ret = [1] * N
        for i in range(N):
            ret[i] = left
            left *= nums[i]
        
        right = 1
        for i in reversed(range(N)):
            ret[i] *= right
            right *= nums[i]

        return ret

if __name__ == "__main__":
    nums = [1,2,3,4]
    solu = Solution()
    print(solu.productExceptSelf(nums))