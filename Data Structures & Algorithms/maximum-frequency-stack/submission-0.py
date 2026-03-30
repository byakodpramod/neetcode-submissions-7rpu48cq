from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.cntMap = defaultdict(int)     # val -> freq
        self.group = defaultdict(list)     # freq -> stack
        self.maxFreq = 0

    def push(self, val: int) -> None:
        freq = self.cntMap[val] + 1
        self.cntMap[val] = freq

        if freq > self.maxFreq:
            self.maxFreq = freq

        self.group[freq].append(val)

    def pop(self) -> int:
        val = self.group[self.maxFreq].pop()
        self.cntMap[val] -= 1

        if not self.group[self.maxFreq]:
            self.maxFreq -= 1

        return val