class Solution {
    private boolean[][] visited;

    private void visit(char[][] grid, int i, int j) {
        if (!visited[i][j]) {
            visited[i][j] = true;
            if (grid[i][j] == '1') {
                if (i < grid.length - 1)
                    visit(grid, i + 1, j);

                if (i > 0)
                    visit(grid, i - 1, j);

                if (j < grid[0].length - 1)
                    visit(grid, i, j + 1);

                if (j > 0)
                    visit(grid, i, j - 1);


            }
        }
    }

    public int numIslands(char[][] grid) {
        int row = grid.length;
        if (row == 0)
            return 0;
        int col = grid[0].length;


        visited = new boolean[row][col];
        int ret = 0;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (!visited[i][j]) {
                    if (grid[i][j] == '1') {
                        ret += 1;
                        visit(grid, i, j);
                    }
                }
            }
        }

        return ret;
    }
}
