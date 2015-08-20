class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        def search(nums, begin, end):
            if begin == end:
                return nums[begin]
            
            mid = int((end - begin)/2)
            pivot = nums[begin]
            
            if pivot > nums[mid]:
                return search(nums, begin, mid)
            else:
                return search(nums, mid + 1, end)
                
        return search(nums, 0, len(nums))
