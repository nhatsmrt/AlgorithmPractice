class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        # Time and Space Complexity: O(N)

        self.children = {id: set() for id in pid}

        for id, par in zip(pid, ppid):
            if par:
                self.children[par].add(id)

        ret = []
        visited = set()

        self.dfs(kill, ret, visited)
        return ret

    def dfs(self, node: int, ret: int, visited: set):
        ret.append(node)

        for child in self.children[node]:
            if child not in visited:
                visited.add(child)
                self.dfs(child, ret, visited)
