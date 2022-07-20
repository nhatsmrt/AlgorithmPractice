OFFSETS = [(0, 0), (0, 1), (1, 0), (-1, 0), (0, -1)]


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        # Time Complexity: O(MN (V + E)) = O(M^2N^2 2^{MN})
        # where V = 2^{MN}, E = O(MN 2^{MN})

        # Space Complexity: O(MNV) = O(MN 2^{MN})

        def mat_to_key(m: List[List[int]]) -> Tuple[Tuple[int]]:
            return tuple(map(tuple, m))

        visited = set()
        traverse = deque()

        init_key = mat_to_key(mat)
        traverse.append((0, mat))
        visited.add(init_key)

        target = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]

        def is_valid(i, j):
            return i >= 0 and i < len(mat) and j >= 0 and j < len(mat[0])

        while traverse:
            dist, cur_mat = traverse.popleft()

            if cur_mat == target:
                return dist

            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    neighbor = deepcopy(cur_mat)

                    for di, dj in OFFSETS:
                        new_i, new_j = i + di, j + dj

                        if is_valid(new_i, new_j):
                            neighbor[new_i][new_j] ^= 1

                    neighbor_key = mat_to_key(neighbor)

                    if neighbor_key not in visited:
                        visited.add(neighbor_key)
                        traverse.append((dist + 1, neighbor))

        return -1
        
