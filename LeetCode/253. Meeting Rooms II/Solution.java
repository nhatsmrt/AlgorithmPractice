class Solution {
    public int minMeetingRooms(int[][] intervals) {
        Set<Event> events = new TreeSet<Event>();
        for (int i = 0; i < intervals.length; i++) {
            events.add(new Event(i, intervals[i][0], true));
            events.add(new Event(i, intervals[i][1], false));
        }

        Set<Integer> happening = new HashSet<Integer>();
        int ret = 0;
        for (Event event : events) {
            if (event.start)
                happening.add(event.ind);
            else
                happening.remove(event.ind);

            if (happening.size() > ret)
                ret = happening.size();
        }

        return ret;
    }


    private class Event implements Comparable<Event> {
        int ind;
        int time;
        boolean start;

        public Event(int ind, int time, boolean start) {
            this.ind = ind;
            this.time = time;
            this.start = start;
        }

        @Override
        public int compareTo(Event other) {
            if (time != other.time)
                return Integer.compare(time, other.time);
            else if (!start && other.start)
                return -1;
            else if (start && !other.start)
                return 1;
            else
                return -1;
        }

        public String toString() {
            return ind + " " + time + " " + start;
        }
    }
}
