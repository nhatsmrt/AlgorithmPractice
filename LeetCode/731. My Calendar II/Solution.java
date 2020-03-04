class MyCalendarTwo {
    // LC's Official Sol
    private TreeMap<Integer, Integer> diffMap;

    public MyCalendarTwo() {
        diffMap = new TreeMap<>();
    }

    public boolean book(int start, int end) {
        diffMap.put(start, diffMap.getOrDefault(start, 0) + 1);
        diffMap.put(end, diffMap.getOrDefault(end, 0) - 1);

        int active = 0;
        for (int d : diffMap.values()) {
            active += d;
            if (active >= 3) {
                diffMap.put(start, diffMap.get(start) - 1);
                diffMap.put(end, diffMap.get(end) + 1);

                if (diffMap.get(start) == 0)
                    diffMap.remove(start);
                return false;
            }
        }

        return true;
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = new MyCalendarTwo();
 * boolean param_1 = obj.book(start,end);
 */s
