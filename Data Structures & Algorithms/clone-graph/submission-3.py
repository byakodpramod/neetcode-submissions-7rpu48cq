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
        q = deque()
        q.append(node)
        while q:
            cur = q.popleft()
            if cur not in store:
                store[node] = Node(cur.val)
            for nei in cur.neighbors:
                if nei not in store:
                    store[nei] = Node(nei.val)
                    q.append(nei)
                store[cur].neighbors.append(store[nei])
        return store[node]