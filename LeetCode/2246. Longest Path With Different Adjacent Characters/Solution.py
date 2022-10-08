def compute_longest_in(node, s, children, in_longest):
    for child in children[node]:
        compute_longest_in(child, s, children, in_longest)

    ret = [0, 0]
    for child in children[node]:
        if s[child] != s[node]:
            child_length = in_longest[child][0] + 1

            if child_length > ret[0]:
                ret = [child_length, ret[0]]
            elif child_length > ret[1]:
                ret[1] = child_length

    in_longest[node] = ret


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        # Time and Space Complexity: O(N)

        children = [[] for i in range(len(parent))]
        root = 0

        for child, par in enumerate(parent):
            if par != -1:
                children[par].append(child)

        in_longest = [None] * len(parent)
        compute_longest_in(root, s, children, in_longest)

        ret = max(1 + sum(children_length) for children_length in in_longest)
        return ret
