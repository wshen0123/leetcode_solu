class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}

    def nSum(self, nums, start, k, t):
        """ Assume nums is sorted
        """
        ret = []
        visited = set()
        if k == 2:
            i = start
            j = len(nums) - 1
            while i < j:
                a = nums[i]
                b = nums[j]
                s = a + b
                if s == t and a not in visited:
                    visited.add(a)
                    ret.append((a,b))
                elif s < t:
                    i += 1
                else:
                    j -= 1
        else:
            for i in range(start, len(nums)):
                v = nums[i]
                if v not in visited:
                    visited.add(v)
                    sub_rets = self.nSum(nums, i+1, k-1, t-v)
                    if sub_rets:
                        for sub_ret in sub_rets:
                            ret.append((v,) + sub_ret)

        return ret    

    def threeSum(self, nums, target):
        nums.sort()
        return self.nSum(nums, 0, 3, target)

    def fourSum(self, nums, target):
        nums.sort()
        return self.nSum(nums, 0, 4, target)
    
if __name__ == "__main__":
    solu = Solution()
    array = [-487,-462,-445,-401,-389,-388,-379,-374,-365,-334,-326,-314,-302,-280,-277,-241,-234,-216,-207,-179,-154,-130,-118,-102,-98,-37,-30,-19,13,21,22,61,66,83,84,109,117,122,141,162,170,205,209,223,232,240,246,250,264,274,286,289,303,304,322,335,336,338,349,355,360,363,365,397,403,417,420,429,438,439]
    array.sort()
    print(solu.fourSum(array, 1801))
