class Solution {
    public List<Integer> minAvailableDuration(int[][] slots1, int[][] slots2, int duration) {
        // time complexity: O(n log n)
        // space complexity: O(n)

        List<Integer> ret = new ArrayList<Integer>();
        Event[] events = new Event[(slots1.length + slots2.length) * 2];
        int cur = 0;
        for (int[] slot : slots1) {
            events[cur] = new Event(slot[0], 1, true);
            events[cur + 1] = new Event(slot[1], 1, false);
            cur += 2;
        }

        for (int[] slot : slots2) {
            events[cur] = new Event(slot[0], 2, true);
            events[cur + 1] = new Event(slot[1], 2, false);
            cur += 2;
        }

        boolean start1 = false;
        boolean start2 = false;
        int prevTime = -1;
        Arrays.sort(events);

        for (int i = 0; i < events.length; i++) {
            Event event = events[i];
            int curTime = event.time;
            if (start1 && start2 && curTime - prevTime >= duration) {
                ret.add(prevTime);
                ret.add(prevTime + duration);
                break;
            }

            prevTime = curTime;
            if (event.person == 1)
                start1 = event.start;
            else
                start2 = event.start;
        }

        return ret;
    }

    private class Event implements Comparable<Event> {
        int time;
        int person;
        boolean start;

        public Event(int time, int person, boolean start) {
            this.time = time;
            this.person = person;
            this.start = start;
        }

        public int compareTo(Event other) {
            return time - other.time;
        }

        public String toString() {
            return "" + time + " " + person + " " + start;
        }
    }
}
