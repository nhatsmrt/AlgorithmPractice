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
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        List<Interval> ret = new ArrayList<Interval>();
        if (intervals.size() == 0 || newInterval.end < intervals.get(0).start) {
            ret.add(newInterval);
            ret.addAll(intervals);
            return ret;
        }
        else if (newInterval.start > intervals.get(intervals.size() - 1).end) {
            ret.addAll(intervals);
            ret.add(newInterval);
            return ret;
        }

        int lower = findLower(intervals, newInterval, 0, intervals.size() - 1);
        int upper = findUpper(intervals, newInterval, 0, intervals.size() - 1);

        for (int i = 0; i <= lower - 1; i++)
            ret.add(intervals.get(i));

        if (isOverlap(intervals.get(lower), newInterval))
            newInterval = mergeTwo(intervals.get(lower), newInterval);
        else
            ret.add(intervals.get(lower));

        for (int i = lower + 1; i <= upper - 1; i++)
            newInterval = mergeTwo(newInterval, intervals.get(i));

        if (isOverlap(intervals.get(upper), newInterval)) {
            newInterval = mergeTwo(intervals.get(upper), newInterval);
            ret.add(newInterval);
        }
        else {
            ret.add(newInterval);
            ret.add(intervals.get(upper));
        }

        for (int i = upper + 1; i < intervals.size(); i++)
            ret.add(intervals.get(i));

        return ret;
    }

    private int findLower(
        List<Interval> intervals,
        Interval newInterval,
        int start, int end
    )
    {
        if (start == end)
            return start;

        int mid = (start + end) / 2;

        if (intervals.get(mid).end > newInterval.start) {
            if (mid == start)
                return mid;
            else
                return findLower(intervals, newInterval, start, mid - 1);
        }

        if (intervals.get(mid + 1).end > newInterval.start)
            return mid;

        return findLower(intervals, newInterval, mid + 1, end);
    }

    private int findUpper(
        List<Interval> intervals,
        Interval newInterval,
        int start, int end
    )
    {
        if (start == end)
            return start;

        int mid = (start + end) / 2;
        if (intervals.get(mid).start < newInterval.end)
            return findUpper(intervals, newInterval, mid + 1, end);
        if (
            mid == start ||
            intervals.get(mid - 1).start < newInterval.end
        )
            return mid;

        return findUpper(intervals, newInterval, start, mid - 1);
    }


    private boolean isOverlap(Interval first, Interval second) {
        return second.start <= first.end && first.start <= second.end;
    }

    // pre: the intervals must overlap
    private Interval mergeTwo(Interval first, Interval second) {
        if (!isOverlap(first, second))
            throw new IllegalArgumentException("Does not overlap!");

        return new Interval(
            Math.min(first.start, second.start),
            Math.max(first.end, second.end)
        );
    }
}
