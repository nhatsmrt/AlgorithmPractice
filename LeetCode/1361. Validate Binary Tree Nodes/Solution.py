class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        adj_lists = {i: set() for i in range(n)}
        par = {i: None for i in range(n)}

        for node, (left, right) in enumerate(zip(leftChild, rightChild)):
            if left != -1:
                if par[left] is not None:
                    return False

                adj_lists[node].add(left)
                par[left] = node

            if right != -1:
                if par[right] is not None:
                    return False

                adj_lists[node].add(right)
                par[right] = node


        root = None
        for node in range(n):
            if par[node] is None:  # root candidate
                if root is not None:  # can't have 2 roots
                    return False

                root = node

        if root is None:
            return False

        visited = set()
        if not self.dfs(root, visited, adj_lists):
            return False

        return len(visited) == n

    def dfs(self, node, visited, adj_lists):
        visited.add(node)

        for neighbor in adj_lists[node]:
            if neighbor in visited:
                return False

            self.dfs(neighbor, visited, adj_lists)

        return True
