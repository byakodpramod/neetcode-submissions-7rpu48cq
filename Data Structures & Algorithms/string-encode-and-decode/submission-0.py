class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            output += str(len(word)) + "#" + word
        return output

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            strLen = int(s[i:j])
            i = j+1
            j = i+strLen
            output.append(s[i:j])
            i = j
        return output