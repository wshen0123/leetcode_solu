from collections import defaultdict

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        if not nums:
            return []
        
        N = len(nums)
        if N <= 2:
            return []
        
        ret = set()
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a = nums[i]
                b = nums[j]
                c = -(a + b)
                if c in d and c >= b:
                    if a == b:
                        if d[a] < 2:
                            continue
                    if b == c:
                        if d[c] < 2:
                            continue
                    if a == c:
                        if d[a] < 3:
                            continue
                    ret.add((a, b, c))
        
        return list(map(list, list(ret)))

if __name__ == "__main__":
    solu = Solution()
    print(solu.threeSum([-1, 0, 1]))
