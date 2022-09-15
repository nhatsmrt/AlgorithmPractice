class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        # Time and Space Complexity: O(MN)

        init_pos = None
        num_key = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "@":
                    init_pos = (i, j)
                elif grid[i][j].islower():
                    num_key += 1

        init_state = (init_pos, tuple([False] * 26))
        traverse = deque()
        traverse.append((init_state, 0))
        visited = {init_state}

        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def is_valid(pos):
            return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])

        def obtain_lock(keyset, lock_pos):
            keyset_lst = list(keyset)
            keyset_lst[lock_pos] = True
            return tuple(keyset_lst)

        while traverse:
            (pos, keyset), dist = traverse.popleft()

            if sum(keyset) == num_key:
                return dist

            for dr, dc in moves:
                new_pos = pos[0] + dr, pos[1] + dc

                if is_valid(new_pos):
                    if grid[new_pos[0]][new_pos[1]] == "#":
                        continue
                    elif grid[new_pos[0]][new_pos[1]].isupper(): # lock
                        if keyset[ord(grid[new_pos[0]][new_pos[1]]) - ord('A')]:
                            new_state = new_pos, keyset
                        else:
                            continue
                    elif grid[new_pos[0]][new_pos[1]].islower(): # key
                        new_state = new_pos, obtain_lock(keyset, ord(grid[new_pos[0]][new_pos[1]]) - ord('a'))
                    elif grid[new_pos[0]][new_pos[1]] in ".@":
                        new_state = new_pos, keyset

                    if new_state not in visited:
                        visited.add(new_state)
                        traverse.append((new_state, dist + 1))

        return -1
