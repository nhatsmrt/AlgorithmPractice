# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        # Time and Space Complexity: O(N)


        parsed_input = []
        parsed_int = []
        openings = []
        match_paren = {}

        for i, char in enumerate(s):
            if char in "-0123456789":
                parsed_int.append(char)
            else:
                if parsed_int:
                    parsed_input.append(int("".join(parsed_int)))
                    parsed_int = []

                parsed_input.append(char)

                if char == "(":
                    openings.append(len(parsed_input) - 1)
                else:
                    last_open = openings.pop()
                    match_paren[last_open] = len(parsed_input) - 1


        if parsed_int:
            parsed_input.append(int("".join(parsed_int)))


        return self.process(parsed_input, 0, len(parsed_input), match_paren)


    def process(self, s, start, end, match_paren) -> TreeNode:
        if start == end:
            return None

        if s[start] == "(":
            return self.process(s, start + 1, end - 1, match_paren)

        # s[start] is int
        if start + 1 == end:
            return TreeNode(s[start])

        left_start = start + 1
        left_end = match_paren[left_start]

        return TreeNode(
            s[start],
            self.process(s, left_start, left_end + 1, match_paren),
            self.process(s, left_end + 1, end, match_paren)
        )
