/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
class Solution {
    public Interval[] intervalIntersection(Interval[] A, Interval[] B) {
        if (A.length == 0 || B.length == 0)
            return new Interval[0];


        List<Interval> ret = new ArrayList<Interval>();

        int i, j;
        i = j = 0;

        while (i < A.length && j < B.length) {
            if (isOverlapped(A[i], B[j])) {
                ret.add(intersect(A[i], B[j]));
                if (A[i].end < B[j].end)
                    i += 1;
                else if (A[i].end > B[j].end)
                    j += 1;
                else {
                    i += 1;
                    j += 1;
                }
            }
            else if (A[i].end < B[j].start)
                i += 1;
            else
                j += 1;
        }

        Interval[] retArr = new Interval[ret.size()];
        retArr = ret.toArray(retArr);
        return retArr;

    }

    private boolean isOverlapped(Interval i1, Interval i2) {
        return i1.end >= i2.start && i2.end >= i1.start;
    }

    private Interval intersect(Interval i1, Interval i2) {
        if (!isOverlapped(i1, i2))
            throw new IllegalArgumentException();

        return new Interval(max(i1.start, i2.start), min(i1.end, i2.end));
    }

    private int min(int a, int b) {
        return a < b ? a : b;
    }

    private int max(int a, int b) {
        return a > b ? a : b;
    }
}
