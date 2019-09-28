class Orange {
    int row;
    int col;

    public Orange(int row, int col) {
        this.row = row;
        this.col = col;
    }

    public String toString() {
        return "[" + row + ", " + col + "]";
    }
}


class Solution {
    public int orangesRotting(int[][] grid) {
        Queue<Orange> orangesRot = new LinkedList<Orange>();
        int fine = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1)
                    fine += 1;
                else if (grid[i][j] == 2)
                    orangesRot.add(new Orange(i, j));
            }
        }

        if (fine == 0)
            return 0;

        int t = 0;

        while (!orangesRot.isEmpty()) {
            Queue<Orange> newRot = new LinkedList<Orange>();

            for (Orange or : orangesRot) {
                int r = or.row;
                int c = or.col;

                if (r > 0 && grid[r - 1][c] == 1) {
                    grid[r - 1][c] = 2;
                    newRot.add(new Orange(r - 1, c));
                    fine -= 1;
                }

                if (r < grid.length - 1 && grid[r + 1][c] == 1) {
                    grid[r + 1][c] = 2;
                    newRot.add(new Orange(r + 1, c));
                    fine -= 1;
                }

                if (c > 0 && grid[r][c - 1] == 1) {
                    grid[r][c - 1] = 2;
                    newRot.add(new Orange(r, c - 1));
                    fine -= 1;
                }

                if (c < grid[0].length - 1 && grid[r][c + 1] == 1) {
                    grid[r][c + 1] = 2;
                    newRot.add(new Orange(r, c + 1));
                    fine -= 1;
                }
            }
            t += 1;
            orangesRot = newRot;
        }

        if (fine != 0)
            return -1;

        return t - 1;
    }
}
