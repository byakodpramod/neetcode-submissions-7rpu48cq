class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                var2 = stack.pop()
                var1 = stack.pop()
                if t == "+":
                    stack.append(var2+var1)
                elif t == "-":
                    stack.append(var1-var2)
                elif t == "*":
                    stack.append(var1*var2)
                elif t == "/":
                    stack.append(int(var1/var2))
            # print(stack)
        return stack[-1]