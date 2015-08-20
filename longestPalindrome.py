class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        def isPalindrome(s):
            #s = "".join(map(lambda c: c.lower(), filter(lambda c: c.isalnum(), s)))
            L = len(s)
            mid = int(L/2)
            
            if L % 2 == 0:
                return s[:mid] == s[-1:-mid-1:-1]
            else:
                return s[:mid] == s[-1:-mid-1:-1]
        
        L = len(s)
        max_len = 0
        if isPalindrome(s):
            return s
        
        for i in range(L):
            for w in range(min(i+1, L-i+1)):
                s_odd = s[i-w:i+w+1]
                s_even = s[i-w:i+w]
                
                if isPalindrome(s_odd):
                    if max_len < 2*w + 1:
                        max_s, max_len = s_odd, 2*w + 1
                else:
                    if isPalindrome(s_even):
                        if max_len < 2*w:
                            max_s, max_len = s_even, 2*w
                    else:
                        break
        return max_s
    
if __name__ == "__main__":
    solu = Solution()
    s = "abababababa"
    print(solu.longestPalindrome(s))