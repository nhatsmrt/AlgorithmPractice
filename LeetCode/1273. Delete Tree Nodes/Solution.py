from typing import Tuple
from functools import reduce


class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        # Time and space complexity: O(N)
        self.children = [[] for i in range(nodes)]
        self.parent, self.value = parent, value

        for i in range(1, nodes):
            self.children[parent[i]].append(i)

        return self.dfs(0)[0]

    def dfs(self, node: int) -> Tuple[int, int, int]:
        # return: number of nodes not removed, and sum
        if len(self.children[node]) == 0:
            if self.value[node] == 0:
                return 0, 0
            else:
                return 1, self.value[node]

        children_result = list(map(self.dfs, self.children[node]))
        if len(children_result) == 1:
            num_nodes = children_result[0][0] + 1
            total_sum = children_result[0][1] + self.value[node]
        else:
            num_nodes = reduce(lambda child1, child2: (child1[0] + child2[0], 0), children_result)[0] + 1
            total_sum = reduce(lambda child1, child2: (0, child1[1] + child2[1]), children_result)[1] + self.value[node]


        if total_sum == 0:
            return 0, total_sum

        return num_nodes, total_sum

        
