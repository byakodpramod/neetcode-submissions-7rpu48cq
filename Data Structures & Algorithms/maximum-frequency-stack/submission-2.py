class FreqStack:

    def __init__(self):
        self.freqMap = defaultdict(int)
        self.cntMap = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        freq = self.freqMap[val]
        self.freqMap[val] += 1
        self.cntMap[freq+1].append(val)
        self.maxFreq = max(self.maxFreq, self.freqMap[val])

    def pop(self) -> int:
        # print(self.cntMap)
        val = self.cntMap[self.maxFreq].pop()
        self.freqMap[val] -= 1
        if len(self.cntMap[self.maxFreq]) == 0:
            self.maxFreq -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()