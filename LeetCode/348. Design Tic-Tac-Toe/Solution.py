class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = []
        self.cols = []

        for _ in range(n):
            self.rows.append(0)
            self.cols.append(0)

        self.main_diag = 0
        self.other_diag = 0
        self.num_moves = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        n = len(self.rows)

        if player == 1:
            self.rows[row] += 1
            self.cols[col] += 1
            if row == col:
                self.main_diag += 1
                if self.main_diag == n:
                    return 1

            if row + col == n - 1:
                self.other_diag += 1
                if self.other_diag == n:
                    return 1
        else:
            self.rows[row] -= 1
            self.cols[col] -= 1

            if row == col:
                self.main_diag -= 1
                if self.main_diag == -n:
                    return 2

            if row + col == n - 1:
                self.other_diag -= 1
                if self.other_diag == -n:
                    return 2

        boardRow = self.rows[row]
        boardCol = self.cols[col]

        if boardRow == n:
            return 1
        elif boardRow == -n:
            return 2

        if boardCol == n:
            return 1
        elif boardCol == -n:
            return 2

        return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
