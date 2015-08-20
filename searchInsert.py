class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            print(left, right)
            mid = int((left + right) / 2)
            
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                break

        print(left, right)
        mid = int((left + right)/2)
        if nums[mid] >= target:
            return mid
        else:
            return mid + 1
