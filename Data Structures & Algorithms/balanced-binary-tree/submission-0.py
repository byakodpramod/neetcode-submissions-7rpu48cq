# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return 0
            lh = helper(root.left)
            rh = helper(root.right)
            if abs(rh-lh) > 1:
                res[0] = False
            return max(lh,rh) + 1
        res = [True]
        helper(root)
        return res[0]