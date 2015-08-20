class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        max_running_sum = nums[0]
        max_global_sum = max_running_sum
        
        for i in nums[1:]:
            max_running_sum = max(max_running_sum + i, i)
            max_global_sum = max(max_global_sum, max_running_sum)
        return max_global_sum
        
        

if __name__ == "__main__":
    solu = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(solu.maxSubArray(nums))
