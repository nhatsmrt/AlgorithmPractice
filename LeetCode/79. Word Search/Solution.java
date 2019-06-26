class Solution {
    private int[][] occupied;
    private char[] toFind;

    public boolean exist(char[][] board, String word) {
        occupied = new int[board.length][board[0].length];
        toFind = word.toCharArray();

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (exist(i, j, board, 0))
                    return true;
            }
        }
        return false;
    }

    private boolean exist(int i, int j, char[][] board, int charInd) {
        if (charInd == toFind.length)
            return true;
        if (
            i < 0 ||
            j < 0 ||
            i >= board.length ||
            j >= board[0].length ||
            occupied[i][j] == 1 ||
            board[i][j] != toFind[charInd]
        )
            return false;

        occupied[i][j] = 1;
        // String newWord = word.substring(1);
        boolean found =
            exist(i - 1, j, board, charInd + 1) ||
            exist(i + 1, j, board, charInd + 1) ||
            exist(i, j - 1, board, charInd + 1) ||
            exist(i, j + 1, board, charInd + 1);
        occupied[i][j] = 0;
        return found;
    }
}
