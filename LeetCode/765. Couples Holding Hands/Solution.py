class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        # Consider each couple a vertex in a graph
        # There is an edge between two couples if there
        # exists a pair of number (row[2i], row[2i + 1])
        # such that each belongs to one of the couple

        # Observation 1: there are N / 2 = edges
        # so # vertices = # couples = # edges

        # Observation 2: Degree of each vertex (couple)
        # is always 2 (self loop is counted twice)
        # This means that the graph is a collection of disjoint cycles
        # (and self-loops)

        # Observation 3: a couple sits next to each other
        # if it belongs to a cycle of length 1/self loop

        # Observation 4: For each cycle, it takes
        # # vertices in cycle - 1 swaps to correct it

        # Time and Space Complexity: O(N)

        adj_lists = {}

        for i in range(0, len(row), 2):
            ver1 = row[i] // 2
            ver2 = row[i + 1] // 2

            if ver1 not in adj_lists:
                adj_lists[ver1] = []

            if ver2 not in adj_lists:
                adj_lists[ver2] = []

            adj_lists[ver1].append(ver2)
            adj_lists[ver2].append(ver1)


        # Cycle decomposition
        ret = 0
        visited = set()

        for i in range(len(row) // 2):
            if i not in visited:
                # new cycle:
                visited.add(i)
                length = 1

                parent = i
                next_ver = adj_lists[i][0]

                while next_ver != i:
                    length += 1
                    visited.add(next_ver)

                    tmp = next_ver
                    if adj_lists[next_ver][0] != parent:
                        next_ver = adj_lists[next_ver][0]
                    else:
                        next_ver = adj_lists[next_ver][1]

                    parent = tmp

                ret += length - 1

        return ret
