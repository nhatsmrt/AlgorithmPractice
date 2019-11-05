class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
        for (int i = 0; i < coordinates.length - 2; i++)
            if (!checkStraightLine(coordinates, i))
                return false;
        return true;
    }

    public boolean checkStraightLine(int[][] coordinates, int i) {
            return
                (coordinates[i + 1][1] - coordinates[i][1]) * (coordinates[i + 2][0] - coordinates[i + 1][0]) == (coordinates[i + 1][0] - coordinates[i][0]) * (coordinates[i + 2][1] - coordinates[i + 1][1]);

    }
}
