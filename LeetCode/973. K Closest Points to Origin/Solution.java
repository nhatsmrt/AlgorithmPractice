class Solution {
    public int[][] kClosest(int[][] points, int K) {
        double[][] dist = new double[points.length][2];
        for (int i = 0; i < points.length; i++) {
            dist[i][0] = Math.sqrt(
                points[i][0] * points[i][0] + points[i][1] * points[i][1]
            );
            dist[i][1] = i;
        }
        Arrays.sort(dist, new Comparator<double[]>() {
            public int compare(double[] point1, double[] point2) {
                return Double.compare(point1[0], point2[0]);
            }
        });

        int[][] ret = new int[K][2];
        for (int i = 0; i < K; i++) {
            ret[i] = points[(int) dist[i][1]];
        }

        return ret;
    }
}
