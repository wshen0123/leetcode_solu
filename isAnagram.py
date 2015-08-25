from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = Counter(list(s))
        t_dict = Counter(list(t))
        
        return sorted(s_dict.items()) == sorted(t_dict.items())

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    solu = Solution()
    print(solu.isAnagram(s, t))