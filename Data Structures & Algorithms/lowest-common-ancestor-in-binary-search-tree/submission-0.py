# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def helper(root):
            if not root:
                return None
            if p.val>root.val and q.val>root.val:
                return helper(root.right)
            if p.val<root.val and q.val<root.val:
                return helper(root.left)
            return root
        return helper(root)