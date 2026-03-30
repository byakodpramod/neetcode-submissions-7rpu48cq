class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return ""
        stack = []
        for ch in s:
            if ch in ("(","[","{"):
                stack.append(ch)
            elif stack and ch == ")":
                if stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            elif stack and ch == "]":
                if stack[-1] != "[":
                    return False
                else:
                    stack.pop()
            elif stack and ch == "}":
                if stack[-1] != "{":
                    return False
                else:
                    stack.pop()
            else:
                return False
        return len(stack) == 0
            