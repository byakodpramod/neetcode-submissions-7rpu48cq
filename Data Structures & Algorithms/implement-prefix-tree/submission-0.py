class PrefixTree:

    def __init__(self):
        self.root = {}
        

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur["#"] = ""

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur:
                return False
            cur = cur[w]
        if "#" in cur:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if w not in cur:
                return False
            cur = cur[w]
        return True
        