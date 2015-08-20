# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        def __isBalanced(root):
            """Return
                -1 if not balanced
                height otherwise
            """
            if not root:
                return 0
            
            if root.left:
                hLeft = __isBalanced(root.left)
                if hLeft < 0:
                    return -1
                else:
                    hLeft += 1
            else:
                hLeft = 0
            
            if root.right:
                hRight = __isBalanced(root.right)
                if hRight < 0:
                    return -1
                else:
                    hRight += 1
            else:
                hRight = 0
            
            if abs(hLeft - hRight) > 1:
                return -1
            else:
                return max(hLeft, hRight)
        
        return __isBalanced(root) > 0

if __name__ == "__main__":
    root = TreeNode(50)
    root.left = TreeNode(17)
    root.right = TreeNode(76)
    root.left.left = TreeNode(9)
    root.left.left.right = TreeNode(14)
    root.left.left.right.left = TreeNode(12)
    root.left.right = TreeNode(23)
    root.left.right.left = TreeNode(19)
    root.right.left = TreeNode(54)
    root.right.left.right = TreeNode(72)
    root.right.left.right.left = TreeNode(67)

    solu = Solution()
    print(solu.isBalanced(root))