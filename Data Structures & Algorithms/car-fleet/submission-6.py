class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        stack = []
        for p,s in reversed(sorted(zip(position,speed))):
            time = (target-p) / s
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)