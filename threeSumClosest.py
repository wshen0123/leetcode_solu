class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        if not nums or len(nums) < 3:
            return None

        nums.sort()
        ret = sum([nums[0], nums[1], nums[-1]])
        N = len(nums)
        for i, a in enumerate(nums[:-2]):
            j = i + 1
            k = N - 1
            while j < k:
                b = nums[j]
                c = nums[k]
                s = a + b + c
                if s == target:
                    return target
                else:
                    if abs(target-s) < abs(target-ret):
                        ret = s
                    if s > target:
                        k -= 1
                    else:
                        j += 1
        return ret


if __name__ == "__main__":
    solu = Solution()
    l, t = [1,1,1,0], 100
    print(solu.threeSumClosest(l, t))
