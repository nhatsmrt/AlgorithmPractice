class Solution {
    private Stack<List<Integer>> moveToGo;
    public void solveSudoku(char[][] board) {
        moveToGo = new Stack<List<Integer>>();
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == '.') {
                    List<Integer> location = new ArrayList<Integer>();
                    location.add(i);
                    location.add(j);
                    moveToGo.push(location);
                }
            }
        }
        move(board);
    }

    private boolean move(char[][] board) {
        if (moveToGo.isEmpty())
            return true;
        else {
            List<Integer> nextMove = moveToGo.pop();
            int i = nextMove.get(0);
            int j = nextMove.get(1);
            for (int k = 1; k < 10; k++) {
                if (isValid(board, i, j, k)) {
                    board[i][j] = (char) (k + '0'); // choose
                    boolean result = move(board); // recursion
                    if (result)
                        return true;
                    else
                        board[i][j] = '.'; // unchoose
                }
            }
            moveToGo.push(nextMove);
            return false;
        }
    }

    private boolean isValid(char[][] board, int i, int j, int k) {
        char c = (char) (k + '0');
        for (int m = 0; m < 9; m ++) {
            if (board[i][m] == c || board[m][j] == c)
                return false;
        }
        int boxH = i / 3;
        int boxW = j / 3;
        for (int h = boxH * 3; h < (boxH + 1) * 3; h++) {
            for (int w = boxW * 3; w < (boxW + 1) * 3; w++) {
                if (board[h][w] == c)
                    return false;
            }
        }

        return true;
    }

}
