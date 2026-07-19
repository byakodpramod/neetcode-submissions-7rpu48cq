class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        open, star = [], []
        for i in range(len(s)):
            if s[i] == "(":
                open.append(i)
            elif s[i] == "*":
                star.append(i)
            else:
                if open and open[-1] < i:
                    open.pop()
                elif star and star[-1] < i:
                    star.pop()
                else:
                    return False
        while open and star:
            if open.pop() > star.pop():
                return False
        return len(open) == 0