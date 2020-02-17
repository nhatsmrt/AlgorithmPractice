from collections import deque


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # print(self.create_state(board))
        initial_state = self.create_state(board)
        # print(self.generate_neighbors(initial_state))

        q = deque()
        q.append((initial_state, 0))
        visited = set()

        while len(q) > 0:
            state, dist = q.popleft()
            if state == "123450":
                return dist
            visited.add(state)
            neighbors = self.generate_neighbors(state)
            for neighbor in neighbors:
                if neighbor not in visited:
                    q.append((neighbor, dist + 1))

        return -1

    def create_state(self, board: List[List[int]]) -> str:
        return ''.join([str(i) for i in board[0]]) + ''.join([str(i) for i in board[1]])

    def generate_neighbors(self, state: str) -> List[str]:
        ret = []
        zero_ind = state.find("0")
        state_list = [char for char in state]
        if zero_ind < 3:
            # move down:
            ret.append(self.swap(state_list, zero_ind, zero_ind + 3))
        if zero_ind > 2:
            # move up
            ret.append(self.swap(state_list, zero_ind, zero_ind - 3))
        if (zero_ind >= 1 and zero_ind <= 2) or zero_ind >= 4:
            # move left
            ret.append(self.swap(state_list, zero_ind, zero_ind - 1))
        if zero_ind <= 1 or (zero_ind >= 3 and zero_ind <= 4):
            # move right:
            ret.append(self.swap(state_list, zero_ind, zero_ind + 1))
        return ret

    def swap(self, state_list: List[str], ind1, ind2) -> str:
            displaced = state_list[ind2]
            state_list[ind2] = '0'
            state_list[ind1] = displaced

            ret = ''.join(state_list)

            state_list[ind1] = '0'
            state_list[ind2] = displaced

            return ret
