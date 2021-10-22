PLAYER_MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def is_adjacent(cur_pos, box_pos):
    return abs(cur_pos[0] - box_pos[0]) + abs(cur_pos[1] - box_pos[1]) == 1

def is_valid(grid, pos):
    return pos[0] >= 0 and pos[0] < len(grid) and pos[1] >= 0 and pos[1] < len(grid[0])

def make_move(cur_pos, box_pos):
    return box_pos, (box_pos[0] - (cur_pos[0] - box_pos[0]), box_pos[1] - (cur_pos[1] - box_pos[1]))


INF = 1000000000


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        # Time Complexity: O(V + E)
        # Space Complexity: O(V)

        # where V = O((MN)^2), E = O(V) = O((MN)^2)

        box_pos = None
        cur_pos = None
        target = None

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == "S":
                    cur_pos = i, j

                if grid[i][j] == "B":
                    box_pos = i, j

                if grid[i][j] == "T":
                    target = i, j

        state = cur_pos, box_pos

        ret = -1
        cur_num_move = 0

        num_move_2_state = {0: set()}
        num_move_2_state[0].add(state)

        state_2_num_move = {}
        state_2_num_move[state] = 0


        while num_move_2_state:
            if not num_move_2_state.get(cur_num_move, []):
                num_move_2_state.pop(cur_num_move)
                cur_num_move += 1
            else:
                state = next(iter(num_move_2_state[cur_num_move]))
                num_move_2_state[cur_num_move].remove(state)
                cur_pos, box_pos = state

                if box_pos == target:
                    return cur_num_move

                for dr, dc in PLAYER_MOVES:
                    new_pos = cur_pos[0] + dr, cur_pos[1] + dc
                    new_state = new_pos, box_pos

                    if is_valid(grid, new_pos) and grid[new_pos[0]][new_pos[1]] != "#" and new_pos != box_pos and state_2_num_move.get(new_state, INF) > cur_num_move:
                        if new_state in state_2_num_move:
                            old_num_move = state_2_num_move[new_state]

                            num_move_2_state[old_num_move].remove(new_state)

                            if not num_move_2_state[old_num_move]:
                                num_move_2_state.pop(old_num_move)

                        state_2_num_move[new_state] = cur_num_move
                        if cur_num_move not in num_move_2_state:
                            num_move_2_state[cur_num_move] = set()

                        num_move_2_state[cur_num_move].add(new_state)

                if is_adjacent(cur_pos, box_pos): # push
                    new_cur_pos, new_box_pos = make_move(cur_pos, box_pos)
                    new_state = new_cur_pos, new_box_pos

                    if is_valid(grid, new_box_pos) and grid[new_box_pos[0]][new_box_pos[1]] != "#" and state_2_num_move.get(new_state, INF) > cur_num_move:
                        if new_state in state_2_num_move:
                            old_num_move = state_2_num_move[new_state]

                            num_move_2_state[old_num_move].remove(new_state)

                            if not num_move_2_state[old_num_move]:
                                num_move_2_state.pop(old_num_move)

                        state_2_num_move[new_state] = cur_num_move + 1
                        if cur_num_move + 1 not in num_move_2_state:
                            num_move_2_state[cur_num_move + 1] = set()

                        num_move_2_state[cur_num_move + 1].add(new_state)

        return -1
