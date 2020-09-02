class Node:
    def __init__(self, data: List[int]):
        self.data, self.ind = data, 0

    def __len__(self):
        return len(self.data)

    def get(self):
        self.ind += 1
        return self.data[self.ind - 1]

    def hasNext(self):
        return self.ind < len(self.data)


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.node1, self.node2 = Node(v1), Node(v2)

        self.node1.next = self.node2
        self.node1.prev = self.node2

        self.node2.next = self.node1
        self.node2.prev = self.node1

        self.it = self.node1
        self.remaining = 2

    def next(self) -> int:
        ret = self.it.get()
        self.it = self.it.next

        return ret


    def hasNext(self) -> bool:
        if not self.remaining:
            return False

        if self.it.hasNext():
            return True
        else:
            # remove the it node
            next_it = self.it.next

            self.it.prev.next = self.it.next
            self.it.next.prev = self.it.prev

            self.it = next_it
            self.remaining -= 1

            return self.hasNext()


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
