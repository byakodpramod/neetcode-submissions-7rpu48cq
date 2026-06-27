# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, curMax):
            if not root:
                return
            curMax = max(curMax, root.val)
            res[0] += root.val >= curMax
            dfs(root.left, curMax)
            dfs(root.right, curMax)
        
        res = [0]
        dfs(root, root.val)
        return res[0]