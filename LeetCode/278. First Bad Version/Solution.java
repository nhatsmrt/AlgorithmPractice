/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        return findBadVersion(1, n);
    }

    private int findBadVersion(int start, int end) {
        if (start == end)
            return start;

        long midLong = ((long) start + end) >> 1;
        int mid = (int) midLong;
        if (super.isBadVersion(mid))
            return findBadVersion(start, mid);
        else
            return findBadVersion(mid + 1, end);
    }
}
