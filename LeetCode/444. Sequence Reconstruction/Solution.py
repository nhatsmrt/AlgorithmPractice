class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # Time Complexity: O(N + sum(len(seqs)))
        # Space Complexity: O(N)

        in_degree = [0] * len(org)
        adj_lists = {i: set() for i in range(1, len(org) + 1)}
        seen = set()

        for seq in seqs:
            for val in seq:
                if val > len(org) or val < 1:
                    return False

                seen.add(val)
            for i in range(1, len(seq)):
                if seq[i] not in adj_lists[seq[i - 1]]:
                    adj_lists[seq[i - 1]].add(seq[i])
                    in_degree[seq[i] - 1] += 1

        if seen != set(org):
            return False

        zero_indegree = set([i for i in range(1, len(org) + 1) if not in_degree[i - 1]])
        for num in org:
            if zero_indegree != set([num]):
                return False

            zero_indegree.remove(num)
            for neighbor in adj_lists[num]:
                in_degree[neighbor - 1] -= 1

                if not in_degree[neighbor - 1]:
                    zero_indegree.add(neighbor)

        return True
