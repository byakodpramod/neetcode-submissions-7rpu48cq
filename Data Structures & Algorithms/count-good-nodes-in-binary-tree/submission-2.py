# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, maxUntil):
            if not root:
                return 0
            res = 1 if root.val >= maxUntil else 0
            maxUntil = max(root.val, maxUntil)
            res += helper(root.left, maxUntil)
            res += helper(root.right, maxUntil)
            return res
        return helper(root, root.val)