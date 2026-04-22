class FreqStack:

    def __init__(self):
        self.freqMap = defaultdict(int)
        self.maxfreq = 0
        self.cntMap = defaultdict(list)

    def push(self, val: int) -> None:
        freq = self.freqMap[val] + 1
        self.freqMap[val] = freq
        if self.maxfreq < freq:
            self.maxfreq = freq
        self.cntMap[freq].append(val)

    def pop(self) -> int:
        val = self.cntMap[self.maxfreq].pop()
        self.freqMap[val] -= 1
        if not self.cntMap[self.maxfreq]:
            self.maxfreq -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()