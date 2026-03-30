# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import *
class Codec:
    
    #Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        def helper(root):
            if not root:
                res.append("#")
                return
            res.append(str(root.val))
            helper(root.left)
            helper(root.right)
        res=[]
        helper(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        def helper(q):
            item = q.popleft()
            if item != "#":
                root = TreeNode(item)
                root.left = helper(q)
                root.right = helper(q)
                return root
            else:
                return None
        # print(data)
        q = deque(data.split(","))
        return helper(q)
