class SnapshotArray {
    // Fat Node Persistent Array
    // Time Complexity: O(1) for set, O(log(M)) for query (where M is the number of sets)
    // Space Complexity: O(N + M)
    private Entry[] data;
    private int time;
    private Map<Integer, Integer> snap2Time;

    public SnapshotArray(int length) {
        data = new Entry[length];
        for (int i = 0; i < length; i++)
            data[i] = new Entry();

        time = 0;
        snap2Time = new HashMap<>();
    }

    public void set(int index, int val) {
        time++;
        data[index].set(val, time);
    }

    public int snap() {
        snap2Time.put(snap2Time.size(), time);
        return snap2Time.size() - 1;
    }

    public int get(int index, int snap_id) {
        int query_time = snap2Time.get(snap_id);
        return data[index].get(query_time);
    }

    private class Entry {
        List<Modification> modList;

        public Entry() {
            modList = new ArrayList<>();
        }

        public void set(int val, int time) {
            modList.add(new Modification(time, val));
        }

        public int get(int time) {
            int insertionPoint = Collections.binarySearch(modList, new Modification(time, -1));
            if (insertionPoint >= 0)
                return modList.get(insertionPoint).val;

            insertionPoint = -insertionPoint - 2;
            if (insertionPoint == -1)
                return 0;
            return modList.get(insertionPoint).val;
        }

        private class Modification implements Comparable<Modification> {
            int time;
            int val;

            public Modification(int time, int val) {
                this.time = time;
                this.val = val;
            }

            public int compareTo(Modification other) {
                return time - other.time;
            }
        }

    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray obj = new SnapshotArray(length);
 * obj.set(index,val);
 * int param_2 = obj.snap();
 * int param_3 = obj.get(index,snap_id);
 */
