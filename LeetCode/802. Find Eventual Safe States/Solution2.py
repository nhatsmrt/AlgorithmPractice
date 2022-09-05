class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Time and Space Complexity: O(V + E)

        outgoing_cnt = [0] * len(graph)
        transposed = {i: set() for i in range(len(graph))}

        for node, outgoing_neigh in enumerate(graph):
            outgoing_cnt[node] += len(outgoing_neigh)

            for neigh in outgoing_neigh:
                transposed[neigh].add(node)

        ret = set()
        no_outgoing = [node for node in range(len(graph)) if outgoing_cnt[node] == 0]

        while no_outgoing:
            node = no_outgoing.pop()
            ret.add(node)

            for neigh in transposed[node]:
                outgoing_cnt[neigh] -= 1

                if outgoing_cnt[neigh] == 0:
                    no_outgoing.append(neigh)

        sorted_ret = []
        for i in range(len(graph)):
            if i in ret:
                sorted_ret.append(i)

        return sorted_ret
