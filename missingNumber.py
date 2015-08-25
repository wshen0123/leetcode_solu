class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        found_N = False
        for i in range(N):
            while nums[i] != i and nums[i] != -1:
                pos = nums[i]
                if nums[i] != N:
                    nums[i], nums[pos] = nums[pos], nums[i]
                else:
                    nums[i] = -1
                    found_N = True
        
        if found_N == False:
            return N
        else:
            for i in range(N):
                if nums[i] == -1:
                    return i
    
if __name__ == "__main__":
    l = [2,1,0]
    solu = Solution()
    print(solu.missingNumber(l))