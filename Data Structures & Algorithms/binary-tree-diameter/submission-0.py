# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return 0
            lh = helper(root.left)
            rh = helper(root.right)
            res[0] = max(res[0], lh+rh+1)
            return max(lh, rh) + 1 
        res = [0]
        helper(root)
        return res[0]-1