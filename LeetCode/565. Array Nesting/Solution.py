class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # Time and Space Complexity: O(N)
        # Idea: the problem can be reduced to finding the size of the largest
        # connected component of a graph
        # with nodes {0,..., N - 1}
        # and edges from i to nums[i] (and nums[i] to i)

        adj_lists = {i: set() for i in range(len(nums))}

        for i in range(len(nums)):
            if nums[i] < len(nums):
                adj_lists[i].add(nums[i])
                adj_lists[nums[i]].add(i)

        visited = set()
        ret = 0

        for i in range(len(nums)):
            if i not in visited:
                ret = max(ret, self.dfs(adj_lists, i, visited))
        return ret

    def dfs(self, adj_lists: dict, node: int, visited: set):
        visited.add(node)
        ret = 1

        for neighbor in adj_lists[node]:
            if neighbor not in visited:
                return 1 + self.dfs(adj_lists, neighbor, visited)

        return ret
