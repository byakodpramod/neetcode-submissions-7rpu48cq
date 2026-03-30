class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        output = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                indexToUpdate, temp = stack.pop()
                output[indexToUpdate] = i - indexToUpdate
            stack.append((i, temperatures[i]))
        return output