class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        # Observation: We can represent the time spent building these blocks using a binary tree
        # where each leaf represents time spent on an individual block
        # each node represent the time spent building the blocks in the leaves in
        # its subtree

        # A node either has two children (split the work) or no children (leaf, does the work)
        # time(node) = time(node.block), if node is leaf;
        # otherwise = split + max(time(node.left), time(node.right))

        # The final value at root (which is the value we need to minimize)
        # is given by:
        # max_{leaf l} split * depth + l.value
        # (this can be proved by structural induction)

        # Greedy algorithm: each time picking the node with min priority,
        # then combine them
        # Proof of correctness: by contradiction

        # Time Complexity: O(n log n)
        # Space Complexity: O(n)

        heap = [block for block in blocks]
        heapq.heapify(heap)

        while len(heap) > 1:
            min1, min2 = heapq.heappop(heap), heapq.heappop(heap)
            heapq.heappush(heap, split + max(min1, min2))

        return heap[0]
