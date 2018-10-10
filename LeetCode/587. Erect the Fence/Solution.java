/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */
class Solution {
    private int exteriorProd(Point a, Point b) {
        return a.x * b.y - a.y * b.x;
    }

    private int signedArea(Point a, Point b, Point c) {
        Point vect1 = new Point(b.x - a.x, b.y - a.y);
        Point vect2 = new Point(c.x - a.x, c.y - a.y);

        return exteriorProd(vect1, vect2);
    }

    private boolean isCounterclockwise(Point a, Point b, Point c) {
        return signedArea(a, b, c) > 0;
    }


    public List<Point> outerTrees(Point[] points) {
        int numPoints = points.length;
        if (numPoints <= 3)
            return Arrays.asList(points);

        // find the point with minimum y-coord
        for (int i = 1; i < numPoints; i++) {
            if ((points[i].y < points[0].y) || (points[i].y == points[0].y && points[i].x < points[0].x)) {
                Point tmp = points[0];
                points[0] = points[i];
                points[i] = tmp;
            }
        }

        Stack<Point> hull = new Stack<Point>();

        List<Point> newList = new ArrayList<Point>();
        for (int i = 1; i < numPoints; i++)
            newList.add(points[i]);
        Collections.sort(newList, new polarComparator(points[0]));




        hull.push(points[0]);
        hull.push(newList.get(0));
        hull.push(newList.get(1));

        ArrayList<Point> deletedPoints = new ArrayList<Point>();
        for (int i = 2; i < numPoints - 1; i++) {
            Point topStack = hull.pop();
            while (!hull.isEmpty() && !isCounterclockwise(hull.peek(), topStack, newList.get(i))) {
                deletedPoints.add(topStack);
                topStack = hull.pop();
            }

            hull.push(topStack);
            hull.push(newList.get(i));
        }

        List<Point> hullList = new ArrayList(hull);

        int numPointInHull = hullList.size();
        for (Point point : deletedPoints) {
            for (int i = 0; i < numPointInHull - 1; i++) {
                if (signedArea(point, hullList.get(i), hullList.get(i + 1)) == 0) {
                    hullList.add(point);
                    break;
                }
            }
            if (signedArea(point, hullList.get(numPointInHull - 1), hullList.get(0)) == 0)
                hullList.add(point);
        }


        return hullList;

    }

    private class polarComparator implements Comparator<Point> {
        private Point anchor;

        public polarComparator(Point anchor) {
            this.anchor = anchor;
        }

        public int compare(Point a, Point b) {
            double angle1 = polarAngle(a);
            double angle2 = polarAngle(b);

            if (angle1 == angle2) {
                if (a.x > b.x)
                    return 1;
                else if (a.x < b.x)
                    return -1;
                else
                    return 0;
            }
            else if (angle1 > angle2)
                return -1;
            else
                return 1;
        }

        private double polarAngle(Point a) {
            double norm = Math.sqrt((double)(a.x - anchor.x) * (double)(a.x - anchor.x) + (double)(a.y - anchor.y) * (double)(a.y - anchor.y));
            return ((double)(a.x - anchor.x)) / norm;
        }
    }
}
