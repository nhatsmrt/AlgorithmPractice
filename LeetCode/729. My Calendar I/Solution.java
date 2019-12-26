class MyCalendar {
    private TreeSet<Interval> data;

    public MyCalendar() {
        data = new TreeSet<>();
    }

    public boolean book(int start, int end) {
        Interval newInterval = new Interval(start, end);
        Interval next = data.ceiling(newInterval);
        Interval previous = data.floor(newInterval);

        boolean overlapped =
            (next != null && newInterval.end > next.start) ||
            (previous != null && newInterval.start < previous.end);

        if (!overlapped)
            data.add(newInterval);
        return !overlapped;
    }

    private class Interval implements Comparable<Interval> {
        int start;
        int end;

        public Interval(int start, int end) {
            this.start = start;
            this.end = end;
        }

        public int compareTo(Interval other) {
            return Integer.compare(start, other.start);
        }

        public String toString() {
            return "[" + start + ", " + end + "]";
        }
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */
