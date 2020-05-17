class QueueNode:
    def __init__(self, val: int):
        self.val = val


class Queue:
    def __init__(self):
        self.front = QueueNode(-1)
        self.rear = QueueNode(-1)
        self.front.next = self.rear
        self.rear.prev = self.front
        self.size = 0

    def append(self, val: int):
        newNode = QueueNode(val)
        newNode.prev = self.rear.prev
        newNode.next = self.rear

        self.rear.prev.next = newNode
        self.rear.prev = newNode

        self.size += 1

    def popleft(self):
        self.front.next.next.prev = self.front
        self.front.next = self.front.next.next
        self.size -= 1

    def suffix_max(self) -> List[int]:
        ret = []
        it = self.rear.prev
        while it != self.front:
            if len(ret) == 0:
                ret.append(it.val)
            else:
                ret.append(max(ret[-1], it.val))
            it = it.prev

        return ret

    def __repr__(self):
        data = []
        it = self.front.next
        while it != self.rear:
            data.append(str(it.val))
            it = it.next

        return ' '.join(data)

    def __len__(self):
        return self.size


class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        # dp[i] = min_{j = 1}^k dp[i - j] + j * max(A[i - j + 1:i + 1])
        # Sparse table allow O(n log n + nk) solution
        # Queue allow O(NK) = O(NK) time and space solution

        sliding_max = []
        queue = Queue()
        for num in A:
            if len(queue) == K:
                queue.popleft()
            queue.append(num)
            sliding_max.append(queue.suffix_max())

        self.dp = [None] * len(A)
        self.sliding_max = sliding_max

        return self.maxPartition(A, len(A) - 1)

    def maxPartition(self, A: List[int], i: int) -> int:
        if i == -1:
            return 0

        if i == 0:
            return A[0]

        if self.dp[i] is not None:
            return self.dp[i]

        ret = -1
        for j in range(len(self.sliding_max[i])):
            ret = max(ret, self.maxPartition(A, i - 1 - j) + (j + 1) * self.sliding_max[i][j])

        self.dp[i] = ret
        return ret
