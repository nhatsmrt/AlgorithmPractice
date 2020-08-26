class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # Time Complexity: O(MN)

        self.moves = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1),
            (1, 1),
            (-1, -1),
            (-1, 1),
            (1, -1)
        ]

        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]]  = "X"
        else:
            self.reveal(board, click[0], click[1])

        return board

    def reveal(self, board: List[List[str]], row: int, col: int) -> List[List[str]]:
        if board[row][col] == "E":
            board[row][col] = "Checking"
            surrounding_mines = self.count_surrounding_mines(board, row, col)


            if surrounding_mines:
                board[row][col] = str(surrounding_mines)
            else:
                board[row][col] = "B"
                for move in self.moves:
                    new_row, new_col = row + move[0], col + move[1]

                    if self.is_valid(board, new_row, new_col):
                        self.reveal(board, new_row, new_col)

    def count_surrounding_mines(self, board: List[List[str]], row: int, col: int) -> int:
        ret = 0

        for move in self.moves:
            new_row, new_col = row + move[0], col + move[1]

            if self.is_valid(board, new_row, new_col) and board[new_row][new_col] == "M":
                ret += 1
        return ret

    def is_valid(self, board: List[List[str]], row: int, col: int) -> bool:
        return row >= 0 and col >= 0 and row < len(board) and col < len(board[0])
