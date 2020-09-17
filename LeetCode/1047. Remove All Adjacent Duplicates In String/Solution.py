class Solution:
    def removeDuplicates(self, S: str) -> str:
        # Time and Space Complexity: O(N)
        stack = []

        for char in S:
            removed = False
            while stack and stack[-1] == char:
                removed = True
                stack.pop()

            if not removed:
                stack.append(char)

        return "".join(stack)
