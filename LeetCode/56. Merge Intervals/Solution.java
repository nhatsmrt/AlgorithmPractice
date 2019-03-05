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
    public List<Interval> merge(List<Interval> intervals) {
        Collections.sort(intervals, new IntervalComparator());
        int ind = 0;
        List<Interval> ret = new ArrayList<Interval>();

        while (ind < intervals.size() - 1) {
            int it = ind + 1;
            Interval newInterval = intervals.get(ind);

            while(it < intervals.size() && isOverlap(newInterval, intervals.get(it))) {
                newInterval = mergeTwo(newInterval, intervals.get(it));
                it += 1;
            }

            ret.add(newInterval);
            ind = it;
        }

        if (ind == intervals.size() - 1)
            ret.add(intervals.get(ind));

        return ret;
    }

    // pre: the intervals must be in order.
    private boolean isOverlap(Interval first, Interval second) {
        return second.start <= first.end;
    }

    // pre: the intervals must overlap
    private Interval mergeTwo(Interval first, Interval second) {
        if (!isOverlap(first, second))
            throw new IllegalArgumentException("Does not overlap!");

        int newStart = first.start;
        int newEnd = first.end > second.end ? first.end : second.end;

        Interval newInterval = new Interval(newStart, newEnd);
        return newInterval;
    }

    private class IntervalComparator implements Comparator<Interval>{
        public int compare(Interval a, Interval b) {
            if (a.start < b.start)
                return -1;
            else if (a.start > b.start)
                return 1;
            else {
                if (a.end < b.end)
                    return -1;
                else if (a.end > b.end)
                    return 1;
                else
                    return 0;
            }
        }
    }
}
