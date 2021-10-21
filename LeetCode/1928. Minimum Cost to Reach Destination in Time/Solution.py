class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        # Time Complexity: O(V' + E')
        # where V' = maxTime x V, and E' = maxTime x E
        # Space Complexity: O(V')

        # Construct an augmented graph, whose nodes are (node, time)
        # and if there is an edge in the original graph from node1 to node2 with travel time t
        # then there are edges in the augmented graph from (node1, time) to (node2, time - t)
        # (if time >= t)

        # The augmented graph is now a DAG, and this problem becomes a DP on DAG problem

        adj_lists = {i: set() for i in range(len(passingFees))}

        for start, end, time in edges:
            adj_lists[start].add((end, time))
            adj_lists[end].add((start, time))

        return self.getCost(maxTime, 0, {}, adj_lists, passingFees)

    def getCost(self, remain: int, node: int, dp, adj_lists, passingFees: List[int]) -> int:
        if (remain, node) in dp:
            return dp[(remain, node)]

        if node == len(passingFees) - 1:
            return passingFees[-1]

        if remain == 0:
            return -1

        ret = -1
        for neigh, time in adj_lists.get(node, []):
            if remain >= time:
                cand_cost = self.getCost(remain - time, neigh, dp, adj_lists, passingFees)

                if cand_cost >= 0 and (ret == -1 or cand_cost < ret):
                    ret = cand_cost

        if ret >= 0:
            ret += passingFees[node]

        dp[(remain, node)] = ret
        return ret
