class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        def isPalindrome(s):
            s = "".join(map(lambda c: c.lower(), filter(lambda c: c.isalnum(), s)))
            L = len(s)
            mid = int(L/2)
            
            if L % 2 == 0:
                return s[:mid] == s[-1:-mid-1:-1]
            else:
                return s[:mid] == s[-1:-mid-1:-1]
        
        L = len(s)
        
        if L == 0:
            return ""
        
        if len(set(s)) == 1:
            return s
        
        first_c = s[0]
        occurance = []
        for i,c in enumerate(s):
            if c == first_c:
                occurance.append(i)
        
        for i in occurance[::-1]:
            if isPalindrome(s[:i+1]):
                break
        
        return s[i+1:][::-1] + s

if __name__ == "__main__":
    solu = Solution()
    s = "a" * 40002
    print(len(s))
    print(solu.shortestPalindrome(s))