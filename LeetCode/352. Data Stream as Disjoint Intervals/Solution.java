class SummaryRanges {
    TreeSet<Interval> intervals;

    /** Initialize your data structure here. */
    public SummaryRanges() {
        // Space Complexity: O(N)
        intervals = new TreeSet<>();
    }

    public void addNum(int val) {
        // Time Complexity: O(log N) per query
        Interval query = new Interval(val, val);
        Interval[] candidates = new Interval[2];

        SortedSet<Interval> tailSet = intervals.tailSet(query);
        SortedSet<Interval> headSet = intervals.headSet(query);

        if (tailSet.size() > 0) {
            candidates[1] = tailSet.first();
        }

        if (headSet.size() > 0) {
            candidates[0] = headSet.last();
        }

        if (candidates[0] != null && candidates[0].end + 1 >= query.start) {
            intervals.remove(candidates[0]);
            query = new Interval(
                Math.min(query.start, candidates[0].start),
                Math.max(query.end, candidates[0].end)
            );
        }

        if (candidates[1] != null && candidates[1].start - 1 <= query.end) {
            intervals.remove(candidates[1]);
            query = new Interval(
                Math.min(query.start, candidates[1].start),
                Math.max(query.end, candidates[1].end)
            );
        }


        intervals.add(query);
    }

    public int[][] getIntervals() {
        // Time Complexity: O(N) per query
        int[][] ret = new int[intervals.size()][2];
        int cnt = 0;

        for (Interval i : intervals) {
            ret[cnt][0] = i.start;
            ret[cnt][1] = i.end;

            cnt += 1;
        }

        return ret;
    }

    private class Interval implements Comparable<Interval> {
        int start;
        int end;

        public Interval(int s, int e) {
            start = s;
            end = e;
        }

        public int compareTo(Interval other) {
            return start - other.start;
        }
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(val);
 * int[][] param_2 = obj.getIntervals();
 */
