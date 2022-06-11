class SegTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None # dynamic
        self.sum = 0
        self.lazy = 0 # lazy prop

    @property
    def size(self):
        return self.end - self.start + 1

    def propagate(self):
        start, end = self.start, self.end

        if self.left is None or self.right is None: # generate the children
            mid = (self.start + self.end) // 2

            self.left = SegTreeNode(start, mid)
            self.right = SegTreeNode(mid + 1, end)

        if self.lazy != 0: # propagate lazy value
            self.left.lazy = self.lazy
            self.right.lazy = self.lazy

            self.left.sum = self.left.size * self.lazy
            self.right.sum = self.right.size * self.lazy

            self.lazy = 0


class SegTree:
    def __init__(self, start: int, end: int):
        self.root = SegTreeNode(start, end)

    def query(self, start, end):
        return self.query_from(self.root, start, end)

    def query_from(self, node, start, end):
        if node.start > end or node.end < start: # no overlapping
            return 0

        if node.start >= start and node.end <= end: # full overlapping
            return node.sum

        # partial overlapping

        if node.lazy == 1: # just returns the overlap size:
            overlap_start = max(start, node.start)
            overlap_end = min(end, node.end)

            return overlap_end - overlap_start + 1

        node.propagate()
        return self.query_from(node.left, start, end) + self.query_from(node.right, start, end)

    def update(self, start, end):
        self.update_from(self.root, start, end)

    def update_from(self, node, start, end):
        if node.start > end or node.end < start: # no overlapping
            return

        if node.lazy == 1: # skip because entire node is already fill
            return

        if node.start >= start and node.end <= end: # full overlapping
            node.lazy = 1 # lazy update
            node.sum = node.size
            return

        # partial overlapping
        node.propagate()
        self.update_from(node.left, start, end)
        self.update_from(node.right, start, end)
        node.sum = node.left.sum + node.right.sum


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        # Time and Space Complexity: O(Q log(MAXVAL - MINVAL))

        low = min(p[0] for p in paint)
        high = max(p[1] for p in paint) - 1

        segtree = SegTree(low, high)
        ret = []

        for start, end in paint:
            old = segtree.query(start, end - 1)
            segtree.update(start, end - 1)
            ret.append(segtree.query(start, end - 1) - old)

        return ret
