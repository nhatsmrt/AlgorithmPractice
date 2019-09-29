class Line {
    private Point point1;
    private Point point2;

    public Line(Point point1, Point point2) {
        this.point1 = point1;
        this.point2 = point2;
    }

    @Override
    public boolean equals(final Object otherObj) {
        if (this == otherObj)
            return true;

        final Line other = (Line) otherObj;

        int slopeDiff = (this.point1.y - this.point2.y) * (other.point1.x - other.point2.x) - (this.point1.x - this.point2.x) * (other.point1.y - other.point2.y);

        if (slopeDiff != 0)
            return false;

        if (this.point1.x == this.point2.x || other.point1.x == other.point2.x) {
                return other.point1.x == other.point2.x
                    && this.point1.x == this.point2.x
                    && other.point1.x == this.point1.x;
        }

        float slope1 = ((float) (this.point1.y - this.point2.y) / (this.point1.x - this.point2.x));
        float slope2 =  ((float) (other.point1.y - other.point2.y) / (other.point1.x - other.point2.x));

        float intercept1 = this.point1.y - this.point1.x * slope1;
        float intercept2 = other.point1.y - other.point1.x * slope2;

        return Math.abs(intercept1 - intercept2) < 0.0000001;
    }

    @Override
    public int hashCode() {
        if (point1.x - point2.x == 0)
            return 100000000;
        else {
            float slope1 = ((float) (this.point1.y - this.point2.y) / (this.point1.x - this.point2.x));
            float intercept1 = this.point1.y - this.point1.x * slope1;

            return (slope1 + " " + intercept1).hashCode();
        }
    }
}


class Point {
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}


class Solution {
    public int maxPoints(int[][] points) {
        if (points.length <= 1)
            return points.length;
        Map<Line, Set<Point>> lineMap = new HashMap<Line, Set<Point>>();

        Point[] pts = new Point[points.length];
        for (int i = 0; i < points.length; i++)
            pts[i] = new Point(points[i][0], points[i][1]);


        for (int i = 0; i < pts.length; i++) {
            for (int j = i + 1; j < pts.length; j++) {
                Line line = new Line(pts[i], pts[j]);
                if (!lineMap.containsKey(line))
                    lineMap.put(line, new HashSet<Point>());

                lineMap.get(line).add(pts[i]);
                lineMap.get(line).add(pts[j]);
            }
        }


        int ret = 0;
        for (Line line : lineMap.keySet()) {
            int candidate = lineMap.get(line).size();
            if (candidate > ret)
                ret = candidate;
        }

        return ret;
    }
}
