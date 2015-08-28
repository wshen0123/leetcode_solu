from memorize import memorize

class Solution(object):
    
    @memorize
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return [eval('a'+c+'b')
            for i, c in enumerate(input) if c in '+-*'
            for a in self.diffWaysToCompute(input[:i])
            for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]

if __name__ == "__main__":
    input = "2*3-4*5"
    solu = Solution()
    print(solu.diffWaysToCompute(input))