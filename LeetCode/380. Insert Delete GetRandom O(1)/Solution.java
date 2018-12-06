class RandomizedSet {
    private Map<Integer, Integer> map; // value to index
    private List<Integer> list; // values

    /** Initialize your data structure here. */
    public RandomizedSet() {
        map = new HashMap<Integer, Integer>();
        list = new ArrayList<Integer>();
    }

    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
        if (map.containsKey(val))
            return false;

        int ind = list.size();
        map.put(val, ind);
        list.add(val);

        return true;
    }

    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
        if (!map.containsKey(val))
            return false;

        int lastInd = list.size() - 1;
        int ind = map.get(val);

        if (ind != lastInd) {
            Integer lastVal = list.get(lastInd);
            list.set(ind, lastVal);
            map.put(lastVal, ind);
        }

        map.remove(val);
        list.remove(lastInd);

        return true;
    }

    /** Get a random element from the set. */
    public int getRandom() {
        return list.get((int) (Math.random() * list.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
