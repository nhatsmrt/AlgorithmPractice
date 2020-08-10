class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        # Preprocessing Time and Space Complexity: O(N log N)

        self.lifting_table = [parent]
        for i in range(int(math.log2(n))):
            new_row = []

            for j in range(n):
                if self.lifting_table[-1][j] == -1:
                    new_row.append(-1)
                else:
                    new_row.append(self.lifting_table[-1][self.lifting_table[-1][j]])

            self.lifting_table.append(new_row)

    def getKthAncestor(self, node: int, k: int) -> int:
        # Query Time Complexity: O(log N)
        if k == 0:
            return node

        row = int(math.log2(k))

        if row > len(self.lifting_table) or self.lifting_table[row][node] == -1:
            return -1

        return self.getKthAncestor(self.lifting_table[row][node], k - 2 ** row)


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
