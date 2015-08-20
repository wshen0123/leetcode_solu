# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.

class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        def generate(begin, end):
            print(begin, end)
            subTrees = []
            
            if begin > end:
                subTrees.append(None)
                return subTrees
            
            for k in range(begin, end + 1):
                leftSubTrees = generate(begin, k - 1)
                rightSubTrees = generate(k + 1, end)
                for leftSubTree in leftSubTrees:
                    for rightSubTree in rightSubTrees:
                        root = TreeNode(k)
                        root.left = leftSubTree
                        root.right = rightSubTree
                        subTrees.append(root)
            return subTrees
        
        return generate(1,n)
        


if __name__ == "__main__":
    solu = Solution()
    print(solu.generateTrees(3))
