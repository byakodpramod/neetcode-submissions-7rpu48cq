# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, curMax):
            if not node:
                return 0
            res[0] += node.val >= curMax
            curMax = max(node.val, curMax)
            helper(node.left, curMax)
            helper(node.right, curMax)
        res = [0]
        helper(root, root.val)
        return res[0]