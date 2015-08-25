class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        path = []
        ret = []
        
        def dfs(root):
            path.append(str(root.val))
            if root.left:
                dfs(root.left)
            
            if root.right:
                dfs(root.right)
            
            if not root.left and not root.right:
                ret.append("->".join(path))
            path.pop()
        
        if root:
            dfs(root)
        
        return ret

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(5)
    
    solu = Solution()
    print(solu.binaryTreePaths(root))