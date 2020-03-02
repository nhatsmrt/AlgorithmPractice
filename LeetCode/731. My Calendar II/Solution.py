class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end

        self.lazy = 0
        self.max = 0


class MyCalendarTwo:

    def __init__(self):
        self.root = Node(0, 1000000000)


    def book(self, start: int, end: int) -> bool:
        max_conflict = self.get_max(self.root, start, end)
        if max_conflict == 2:
            return False

        self.add(self.root, start, end)
        return True

    def get_max(self, node, start, end):
        if node.end <= start or end <= node.start:
            return -1

        if node.lazy != -1:
            return node.lazy

        if start <= node.start and node.end <= end:
            return node.max
        else:
            candidates = []
            candidates.append(self.get_max(node.left, start, end))
            candidates.append(self.get_max(node.right, start, end))
            return max(candidates)

    def add(self, node, start, end):
        if node.end <= start or end <= node.start:
            return

        if node.lazy != -1 and start <= node.start and node.end <= end:
            node.lazy += 1
        else:
            mid = (node.start + node.end) // 2

            if node.lazy != -1:
                node.left = Node(node.start, mid)
                node.right = Node(mid, node.end)

                node.left.lazy = node.lazy
                node.right.lazy = node.lazy
                node.max = node.lazy

                node.lazy = -1

            self.add(node.left, start, end)
            self.add(node.right, start, end)

            node.max = max(
                [node.max, node.left.lazy, node.left.max, node.right.lazy, node.right.max]
            )
