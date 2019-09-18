class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        if (newColor == image[sr][sc])
            return image;

        floodFill(image, sr, sc, newColor, image[sr][sc]);
        return image;
    }

    private void floodFill(int[][] image, int i, int j, int newColor, int oldColor) {
        image[i][j] = newColor;

        if (i > 0 && image[i - 1][j] == oldColor)
            floodFill(image, i - 1, j, newColor, oldColor);

        if (i < image.length - 1 && image[i + 1][j] == oldColor)
            floodFill(image, i + 1, j, newColor, oldColor);

        if (j > 0 && image[i][j - 1] == oldColor)
            floodFill(image, i, j - 1, newColor, oldColor);

        if (j < image[0].length - 1 && image[i][j + 1] == oldColor)
            floodFill(image, i, j + 1, newColor, oldColor);

    }
}
