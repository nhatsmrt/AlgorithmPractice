class Solution {
    public void gameOfLife(int[][] board) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                int neighbors = 0;
                if (i > 0) {
                    neighbors += board[i - 1][j] % 2;
                    if (j > 0)
                        neighbors += board[i - 1][j - 1] % 2;

                    if (j < board[0].length - 1)
                        neighbors += board[i - 1][j + 1] % 2;
                }

                if (i < board.length - 1) {
                    neighbors += board[i + 1][j] % 2;

                    if (j > 0)
                        neighbors += board[i + 1][j - 1] % 2;

                    if (j < board[0].length - 1)
                        neighbors += board[i + 1][j + 1] % 2;
                }

                if (j > 0)
                    neighbors += board[i][j - 1] % 2;

                if (j < board[0].length - 1)
                    neighbors += board[i][j + 1] % 2;


                if (board[i][j] == 0) {
                    if (neighbors == 3)
                        board[i][j] = 4;
                }
                else {
                    if (neighbors < 2 || neighbors > 3)
                        board[i][j] = 3;
                }
            }
        }

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++)
                board[i][j] %= 3;
        }
    }
}
