# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxUntil):
            if not node:
                return 0
            res[0] += node.val >= maxUntil
            dfs(node.left, max(maxUntil, node.val))
            dfs(node.right, max(maxUntil, node.val))
        res = [0]
        dfs(root, float("-inf"))
        return res[0]