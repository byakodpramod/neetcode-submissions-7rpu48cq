"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        store = {}
        q = deque([node])
        while q:
            curNode = q.popleft()
            if curNode not in store:
                store[curNode] = Node(node.val)
            for neigh in curNode.neighbors:
                if neigh not in store:
                    store[neigh] = Node(neigh.val)
                    q.append(neigh)
                store[curNode].neighbors.append(store[neigh])
        return store[node]
