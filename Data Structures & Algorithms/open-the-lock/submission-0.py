class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        def children(lock):
            res = []
            for i in range(4):
                digit = (int(lock[i]) + 1) % 10
                res.append(lock[:i]+str(digit)+lock[i+1:])
                digit = (int(lock[i]) - 1 + 10) % 10
                res.append(lock[:i]+str(digit)+lock[i+1:])
            return res
        q = deque()
        q.append(("0000", 0))
        visited = set(deadends)
        visited.add("0000")
        res = float("inf")
        while q:
            curNum, turn = q.popleft()
            if curNum == target:
                res = min(res, turn)
            for num in children(curNum):
                if num not in visited:
                    visited.add(num)
                    q.append((num, turn+1))
        return res if res != float('inf') else -1