class Solution {
    private double radius;
    private double x_center;
    private double y_center;
    private Random randomizer;

    public Solution(double radius, double x_center, double y_center) {
        this.radius = radius;
        this.x_center = x_center;
        this.y_center = y_center;
        randomizer = new Random();
    }

    public double[] randPoint() {
        boolean found = false;
        double[] ret = new double[2];

        while (!found) {
            double x = randomizer.nextDouble() * 2 * radius + x_center - radius;
            double y = randomizer.nextDouble() * 2 * radius + y_center - radius;

            if ((x_center - x) * (x_center - x) + (y_center - y) * (y_center - y) <= radius * radius) {
                ret[0] = x;
                ret[1] = y;
                found = true;
            }
        }

        return ret;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(radius, x_center, y_center);
 * double[] param_1 = obj.randPoint();
 */
