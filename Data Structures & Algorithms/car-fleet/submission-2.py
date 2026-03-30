import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse=True)
        stack = []
        for pos,sp in pair:
            time = (target-pos)/sp
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)