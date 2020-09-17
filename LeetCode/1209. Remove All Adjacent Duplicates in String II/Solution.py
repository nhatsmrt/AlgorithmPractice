class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Time and Space Complexity: O(N)

        stack = []
        adj_cnt = []

        for char in s:
            if stack and char == stack[-1]:
                adj_cnt[-1] += 1
            else:
                adj_cnt.append(1)

            stack.append(char)

            if adj_cnt[-1] == k:
                for _ in range(k):
                    stack.pop()
                adj_cnt.pop()

        return "".join(stack)
