import collections

class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        L1 = len(s1)
        L2 = len(s2)
        
        if L1 != L2:
            return False
        
        if L1 == 1:
            return s1 == s2
        
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        for c in s1:
            d1[c] += 1
        for c in s2:
            d2[c] += 1
        for k,v in d1.items():
            if d2[k] != v:
                return False
            
        if L1 <= 3:
            return True
        
        for i in range(1, L1):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or (self.isScramble(s1[-i:], s2[:i]) and self.isScramble(s1[:i], s2[-i])):
                return True
        
        return False

if __name__ == "__main__":
    solu = Solution()
    s1 = "xstjzkfpkggnhjzkpfjoguxvkbuopi"
    s2 = "xbouipkvxugojfpkzjhnggkpfkzjts"
    print(solu.isScramble(s1, s2))
