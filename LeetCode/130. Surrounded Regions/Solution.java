class Solution {
    public void solve(char[][] board) {
        if (board.length == 0)
            return;

        for (int i = 0; i < board.length; i++) {
            if (board[i][0] == 'O')
                floodFill(board, i, 0);

            if (board[i][board[0].length - 1] == 'O')
                floodFill(board, i, board[0].length - 1);
        }

        for (int j = 0; j < board[0].length; j++) {
            if (board[0][j] == 'O')
                floodFill(board, 0, j);

            if (board[board.length - 1][j] == 'O')
                floodFill(board, board.length - 1, j);
        }

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == 'O')
                    board[i][j] = 'X';

                if (board[i][j] == 'A')
                    board[i][j] = 'O';
            }
        }
    }

    private void floodFill(char[][] board, int i, int j) {
        board[i][j] = 'A';

        if (i > 0 && board[i - 1][j] == 'O')
            floodFill(board, i - 1, j);

        if (i < board.length - 1 && board[i + 1][j] == 'O')
            floodFill(board, i + 1, j);

        if (j > 0 && board[i][j - 1] == 'O')
            floodFill(board, i, j - 1);

        if (j < board[0].length - 1 && board[i][j + 1] == 'O')
            floodFill(board, i, j + 1);
    }
}
