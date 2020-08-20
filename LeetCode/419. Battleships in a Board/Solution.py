class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ret = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.is_head(board, i, j):
                    ret += 1

        return ret

    def is_head(self, board: List[List[str]], i: int, j: int) -> bool:
        if board[i][j] == ".":
            return False

        if i > 0 and board[i - 1][j] == "X":
            return False

        if j > 0 and board[i][j - 1] == "X":
            return False

        return True
