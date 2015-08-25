class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        INT_LEN = 32
        count_digit = [0] * INT_LEN
        count_sign = 0
        for n in nums:
            if n < 0:
                count_sign += 1
                n = -n
            
            for i in range(INT_LEN-1, -1, -1):
                count_digit[i] += (n & 1)
                n >>= 1
        
        ret = 0
        for i,b in enumerate(count_digit):
            if b % 3 != 0:
                ret += 1<<(31-i)
        
        return ret * (-1 if count_sign % 3 == 1 else 1)


if __name__ == "__main__":
    nums = [-401451,-177656,-2147483646,-473874,-814645,-2147483646,-852036,-457533,-401451,-473874,-401451,-216555,-917279,-457533,-852036,-457533,-177656,-2147483646,-177656,-917279,-473874,-852036,-917279,-216555,-814645,2147483645,-2147483648,2147483645,-814645,2147483645,-216555]
    
    solu = Solution()
    print(solu.singleNumber(nums))