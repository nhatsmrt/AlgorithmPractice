class Solution {
    public int diagonalSum(int[][] mat) {
        List<Integer> values = new ArrayList<>();

        for (int i = 0; i < mat.length; i++) {
            values.add(mat[i][i]);

            if (mat.length - 1 - i != i)
                values.add(mat[i][mat.length - 1 - i]);
        }

        return values.stream().reduce(0, (x, y) -> x + y);
    }
}
