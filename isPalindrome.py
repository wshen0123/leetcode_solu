class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        s = "".join(map(lambda c: c.lower(), filter(lambda c: c.isalnum(), s)))
        L = len(s)
        mid = int(L/2)
        
        if L % 2 == 0:
            return s[:mid] == s[-1:-mid-1:-1]
        else:
            return s[:mid] == s[-1:-mid-1:-1]

if __name__ == "__main__":
    solu = Solution()
    s = "race a car"
    print(solu.isPalindrome(s))