class Solution {
    public int minAreaRect(int[][] points) {
        // Time Complexity: O(n^2)
        // Space Complexity: O(n)
        Set<Point> pts = new HashSet<Point>();
        for (int[] point : points)
            pts.add(new Point(point[0], point[1]));

        int ret = 0;
        for (Point pt1 : pts) {
            for (Point pt2 : pts) {
                if (pt1.x != pt2.x && pt1.y != pt2.y) {
                    Point pt3 = new Point(pt1.x, pt2.y);
                    Point pt4 = new Point(pt2.x, pt1.y);
                    if (pts.contains(pt3) && pts.contains(pt4)) {
                        int candidateArea = Math.abs(pt1.x - pt2.x) *  Math.abs(pt1.y - pt2.y);
                        if (ret == 0 || ret > candidateArea)
                            ret = candidateArea;
                    }
                }
            }
        }

        return ret;
    }

    private class Point {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public boolean equals(Object otherObj) {
            Point other = (Point) otherObj;
            return x == other.x && y == other.y;
        }

        public int hashCode() {
            return x * 1000000007 + y;
        }
    }
}
