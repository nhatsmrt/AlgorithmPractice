class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # Time Complexity: O(N) + O(4 * 8 * N) = O(N)
        # Space Complexity: O(N)

        cur_level = 0
        cur_level_genes = set([start])
        remain = set(bank)
        choices = ["A", "C", "T", "G"]

        while cur_level_genes:
            next_level = set()

            for gene in cur_level_genes:
                if gene == end:
                    return cur_level
                else:
                    for i in range(8):
                        for choice in choices:
                            if choice != gene[i]:
                                neighbor = gene[:i] + choice + gene[i + 1:]

                                if neighbor in remain:
                                    remain.remove(neighbor)
                                    next_level.add(neighbor)

            cur_level += 1
            cur_level_genes = next_level

        return -1
