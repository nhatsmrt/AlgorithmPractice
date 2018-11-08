class Board {
    private ArrayList<String> board;

    public Board(int size) {
        if (size <= 0)
            throw new IllegalArgumentException();

        board = new ArrayList<String>();
        for (int i = 0; i < size; i++) {
            String row = "";
            for (int j = 0; j < size; j++)
                row += ".";
            board.add(row);
        }
    }

    public ArrayList<String> getBoard() {
        return  (ArrayList) board.clone();
    }

    public void place(int row, int col) {
        if (!isSafe(row, col) || board.get(row).charAt(col) == 'Q')
            throw new IllegalArgumentException("Invalid move");

        board.set(row, board.get(row).substring(0, col) + "Q" + board.get(row).substring(col + 1));
    }

    public void remove(int row, int col) {
        if (!withinBound(row, col) || board.get(row).charAt(col) != 'Q')
            throw new IllegalArgumentException("Invalid remove");

        board.set(row, board.get(row).substring(0, col) + "." + board.get(row).substring(col + 1));
    }

    public boolean isSafe(int row, int col) {
        return withinBound(row, col) && rowLegal(row) && colLegal(col) && diagLegal(row, col);
    }

    public int size() {
        return board.size();
    }

    private boolean withinBound(int row, int col) {
        return row >= 0 && row < board.size() && col >= 0 && col < board.size();
    }

    private boolean rowLegal(int row) {
        if (row < 0 || row >= board.size())
            throw new IllegalArgumentException();

        return board.get(row).indexOf("Q") == -1;
    }

    private boolean colLegal(int col) {
        if (col < 0 || col >= board.size())
            throw new IllegalArgumentException();

        for (int i = 0; i < board.size(); i++) {
            if(board.get(i).charAt(col) == 'Q')
                return false;
        }
        return true;
    }

    private boolean diagLegal(int row, int col) {
        if (!withinBound(row, col))
            throw new IllegalArgumentException();

        for (int i = 1; i <= Math.min(row, col); i++) {
            if (board.get(row - i).charAt(col - i) == 'Q')
                return false;
        }

        for (int i = 1; i < board.size() - Math.max(row, col); i++) {
            if (board.get(row + i).charAt(col + i) == 'Q')
                return false;
        }

        for (int i = 1; i < Math.min(row + 1, board.size() - col); i++) {
            if (board.get(row - i).charAt(col + i) == 'Q')
                return false;
        }

        for (int i = 1; i < Math.min(col + 1, board.size() - row); i++) {
            if (board.get(row + i).charAt(col - i) == 'Q')
                return false;
        }

        return true;
    }
}

class Solution {
    public int totalNQueens(int n) {
        if (n < 2)
            return n;

        return exploreOptions(new Board(n), 0);
    }

    private int exploreOptions(Board b, int col) {
        int ret = 0;

        if (col == b.size()) {
            return 1;
        }
        else {
            for (int i = 0; i < b.size(); i++) {
                if (b.isSafe(i, col)) {
                    b.place(i, col);
                    ret += exploreOptions(b, col + 1);
                    b.remove(i, col);
                }
            }
            return ret;
        }
    }

}
