class Solution2 {
    private double radiusSq;
    private double x;
    private double y;
    private Random randomizer;

    public Solution(double radius, double x_center, double y_center) {
        radiusSq = radius * radius;
        x = x_center;
        y = y_center;
        randomizer = new Random();
    }

    public double[] randPoint() {
        double[] ret = new double[2];

        double dist = Math.sqrt(randomizer.nextDouble() * radiusSq);
        double theta = randomizer.nextDouble() * 2 * Math.PI;

        ret[0] = x + Math.cos(theta) * dist;
        ret[1] = y + Math.sin(theta) * dist;
        return ret;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(radius, x_center, y_center);
 * double[] param_1 = obj.randPoint();
 */
