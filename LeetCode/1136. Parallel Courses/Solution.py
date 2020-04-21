class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        adj_lists = {}
        no_prereq = set([i for i in range(1, N + 1)])

        for relation in relations:
            if relation[0] not in adj_lists:
                adj_lists[relation[0]] = set()


            adj_lists[relation[0]].add(relation[1])

            if relation[1] in no_prereq:
                no_prereq.remove(relation[1])

        unvisited = set([i for i in range(1, N + 1)])
        while len(unvisited) > 0:
            dfs_root = unvisited.pop()
            if not self.dfs(dfs_root, set(), unvisited, adj_lists):
                return -1

        # dp[node] = longest path from node in the DAG
        self.dp = {}
        self.adj_lists = adj_lists
        ret = 0
        for course in no_prereq:
            ret = max(ret, self.longest_path(course))

        return ret

    def dfs(self, node: int, ancestor: set, unvisited: dict, adj_lists: dict):
        if node not in adj_lists:
            return True

        ancestor.add(node)
        for child in adj_lists[node]:
            if child in ancestor:
                return False

            if child in unvisited:
                unvisited.remove(child)
                if not self.dfs(child, ancestor, unvisited, adj_lists):
                    return False

        ancestor.remove(node)
        return True

    def longest_path(self, node: int) -> int:
        if node in self.dp:
            return self.dp[node]

        ret = 0
        for child in self.adj_lists.get(node, []):
            ret = max(ret, self.longest_path(child))

        ret += 1
        self.dp[node] = ret

        return ret


    
