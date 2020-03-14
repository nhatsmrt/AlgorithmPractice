class Node:
    def __init__(self, lower, upper):
        self.lower, self.upper = lower, upper
        self.left, self.right = None, None
        self.lazy = True
        self.is_tracked = False

    def __repr__(self):
        return str(self.lower) + "_" + str(self.upper)


class RangeModule:

    def __init__(self):
        self.root = Node(0, 1000000000)


    def addRange(self, left: int, right: int) -> None:
        self.change(self.root, left, right, True)

    def queryRange(self, left: int, right: int) -> bool:
        return self.query(self.root, left, right)

    def removeRange(self, left: int, right: int) -> None:
        self.change(self.root, left, right, False)

    def query(self, node: Node, lower, upper) -> bool:
        if node.upper <= lower or node.lower >= upper:
            return True

        if node.is_tracked:
            return True

        if (node.lower >= lower and node.upper <= upper) or node.lazy:
            return node.is_tracked

        return self.query(node.left, lower, upper) and self.query(node.right, lower, upper)


    def change(self, node: Node, lower: int, upper: int, tracked: bool):
        if node.upper <= lower or node.lower >= upper:
            return

        if node.lower >= lower and node.upper <= upper:
            node.is_tracked = tracked
            node.lazy = True
            return

        if node.left is None:
            mid = node.lower + (node.upper - node.lower) // 2
            node.left = Node(node.lower, mid)
            node.right = Node(mid, node.upper)

        if node.lazy:
            node.left.is_tracked = node.right.is_tracked = node.is_tracked
            node.left.lazy = node.right.lazy = True
            node.lazy = False

        self.change(node.left, lower, upper, tracked)
        self.change(node.right, lower, upper, tracked)
        node.is_tracked = node.left.is_tracked and node.right.is_tracked



# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
