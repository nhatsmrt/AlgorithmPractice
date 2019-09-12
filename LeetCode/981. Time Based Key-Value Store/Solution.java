class TimeMap {
    Map<String, TreeMap<Integer, String>> data;
    /** Initialize your data structure here. */
    public TimeMap() {
        data = new HashMap<String, TreeMap<Integer, String>>();
    }

    public void set(String key, String value, int timestamp) {
        if (!data.containsKey(key))
            data.put(key, new TreeMap<Integer, String>());
        data.get(key).put(timestamp, value);
    }

    public String get(String key, int timestamp) {
        if (!data.containsKey(key))
            return "";
        TreeMap<Integer, String> tree = data.get(key);
        Integer closest = tree.floorKey(timestamp);
        if (closest == null)
            return "";
        return tree.get(closest);
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */
