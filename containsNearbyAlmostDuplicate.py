class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    
    
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        G = {"found":False}
        
        class TreeNode:
            def __init__(self, index, val):
                self.val = val
                self.index = index
                self.left = None
                self.right = None
            
        def buildBST(bst, i, n, k, t):
            if not bst:
                return TreeNode(i, n)
            
            if abs(bst.val-n) <= t and abs(bst.index-i) <= k:
                G["found"] = True
                return
            
            if bst.val > n:
                bst.left = buildBST(bst.left, i, n, k, t)
            elif bst.val < n:
                bst.right = buildBST(bst.right, i, n, k, t)
            else:
                bst.index = i
            
            return bst
        
        bst = None
        for i,n in enumerate(nums):
            bst = buildBST(bst, i, n, k, t)
            if G["found"]:
                return True
        return False

if __name__ == "__main__":
    nums, k, t = [10,100,11,9], 1, 2
    solu = Solution()
    print(solu.containsNearbyAlmostDuplicate(nums, k, t))