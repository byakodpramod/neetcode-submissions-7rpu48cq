class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")
        print(paths)
        for item in paths:
            if item == "..":
                if stack:
                    stack.pop()
            elif item != "" and item != ".":
                stack.append(item)
        return "/"+"/".join(stack)