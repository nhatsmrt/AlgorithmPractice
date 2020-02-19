class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        components = path.split("/")

        for component in components:
            if len(component) > 0:
                if component == "..":
                    if len(stack) > 0:
                        stack.pop()
                elif component != '.':
                    stack.append(component)

        return "/" + "/".join(stack)
