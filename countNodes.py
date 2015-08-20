
"""
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last,
is completely filled, and all nodes in the last level are as far
left as possible. It can have between 1 and 2h nodes inclusive at
 the last level h.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        def heightLeft(root):
            if not root:
                return 0
            height = 0
            while root:
                height += 1
                root = root.left
            return height
        
        def traceNode(root, height, path):
            #print("traceNode", height, path)
            while root and height:
                if path & (1<<(height-1)):
                    root = root.right
                else:
                    root = root.left
                height -= 1
            return root
        
        h = heightLeft(root)
        if h == 0:
            return 0

        left = 0
        right = (1 << (h-1)) - 1
        while left <= right:
            mid = int((left + right) / 2)
            #print(left, mid, right)
            if traceNode(root, h-1, mid):
                left = mid + 1
                #print("left")
            else:
                right = mid - 1
                #print("right")
                
        #print(h, right)
        return (1 << (h - 1)) + right 

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
#     root.left.right = TreeNode(5)
#     root.right.left = TreeNode(6)
    
    solu = Solution()
    print(solu.countNodes(root))