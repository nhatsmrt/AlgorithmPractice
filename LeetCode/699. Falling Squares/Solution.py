class Node:
    def __init__(self, low, high):
        self.low, self.high = low, high
        self.lazy = 0
        self.val = 0
        self.left, self.right = None, None

    def __repr__(self):
        ret = str([str(self.low), str(self.high), str(self.lazy), str(self.val)])
        if self.left is not None:
            ret += " " + self.left.__repr__() + " " + self.right.__repr__()
        return ret


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        root = Node(0, 200000000)

        res = [0]
        for position in positions:
            low, high = position[0], position[0] + position[1]
            max_in_range = self.query(root, low, high)
            self.update(root, low, high, position[1] + max_in_range)
            height = root.lazy + root.val
            res.append(max(max(res), height))

        return res[1:]

    def update(self, node: Node, low: int, high: int, val: int):
        if low < node.high and node.low < high:
            if low <= node.low and node.high <= high:
                node.lazy = val
                node.val = 0
                node.left = node.right = None
            else:
                # Push down:
                self.pushdown(node)

                # Update:
                self.update(node.left, low, high, val)
                self.update(node.right, low, high, val)
                node.val = max(node.left.val + node.left.lazy, node.right.val + node.right.lazy)

    def query(self, node: Node, low: int, high: int):
        if node.low >= high or node.high <= low:
            return 0

        if (low <= node.low and node.high <= high) or node.left is None:
            return node.lazy + node.val

        return max(self.query(node.left, low, high), self.query(node.right, low, high)) + node.lazy

    def pushdown(self, node: Node):
        if node.left is None:
            mid = node.low + (node.high - node.low) // 2
            node.left, node.right = Node(node.low, mid), Node(mid, node.high)

        node.left.lazy += node.lazy
        node.right.lazy += node.lazy
        node.lazy = 0
        node.val = max(node.left.val + node.left.lazy, node.right.val + node.right.lazy)

        
