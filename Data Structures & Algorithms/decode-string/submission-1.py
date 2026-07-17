class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""
        curNum, curS, stack = 0, "", []
        for i in range(len(s)):
            if s[i].isdigit():
                curNum = curNum*10 + int(s[i])
                continue
            elif s[i] == "[":
                stack.append((curNum, curS))
                curNum = 0
                curS = ""
            elif s[i] == "]":
                if stack:
                    prevN, prevS = stack.pop()
                    curS = prevS + (curS*prevN)
            else:
                curS += s[i]
        return curS
