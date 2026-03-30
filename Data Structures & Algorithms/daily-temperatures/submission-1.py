class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        output = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                temp, idx = stack.pop()
                output[idx] = i - idx
            stack.append((temperatures[i], i))
        return output