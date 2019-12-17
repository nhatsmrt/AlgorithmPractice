class HitCounter {
    private Queue<Integer> hits;

    /** Initialize your data structure here. */
    public HitCounter() {
        hits = new LinkedList<Integer>();
    }

    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    public void hit(int timestamp) {
        while(!hits.isEmpty() && hits.peek() + 300 <= timestamp)
            hits.remove();
        hits.add(timestamp);
    }

    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    public int getHits(int timestamp) {
        while(!hits.isEmpty() && hits.peek() + 300 <= timestamp)
            hits.remove();
        return hits.size();
    }
}

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter obj = new HitCounter();
 * obj.hit(timestamp);
 * int param_2 = obj.getHits(timestamp);
 */
