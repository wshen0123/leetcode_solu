class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        num = [0] * n
        seq = []
        visited = set()

        def bt(k):
            if k == 2**n:
                return True
            for i in range(n):
                num[i] ^= 1
                curr = int("".join([str(c) for c in num]), 2)
                if curr not in visited:
                    visited.add(curr)
                    seq.append(curr)
                    if bt(k+1) == True:
                        return True
                    else:
                        visited.remove(curr)
                        seq.removed(curr)
                num[i] ^= 1

        bt(0)
        return seq

if __name__ == "__main__":
    solu = Solution()
    print(solu.grayCode(10))
                
                
                    
        
