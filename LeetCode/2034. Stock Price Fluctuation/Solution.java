import java.util.SortedMap;

class StockPrice {
    private SortedMap <Integer, Integer> timeToPrice;
    private SortedMap <Integer, Set<Integer>> priceToTime;
    private int curTime;
    private int curPrice;

    public StockPrice() {
        // Space Complexity: O(N)
        curTime = 0;
        curPrice = 0;

        timeToPrice = new TreeMap<>();
        priceToTime = new TreeMap<>();
    }

    public void update(int timestamp, int price) {
        // Time Complexity: O(log N)

        if (timestamp >= curTime) {
            curTime = timestamp;
            curPrice = price;
        }

        if (timeToPrice.containsKey(timestamp)) { // correction
            int oldPrice = timeToPrice.get(timestamp);
            priceToTime.get(oldPrice).remove(timestamp);

            if (priceToTime.get(oldPrice).isEmpty()) {
                priceToTime.remove(oldPrice);
            }
        }

        timeToPrice.put(timestamp, price);

        if (!priceToTime.containsKey(price)) {
            priceToTime.put(price, new HashSet<>());
        }
        priceToTime.get(price).add(timestamp);
    }

    public int current() {
        // Time Complexity: O(1)
        return curPrice;
    }

    public int maximum() {
        // Time Complexity: O(log N)
        return priceToTime.lastKey();
    }

    public int minimum() {
        // Time Complexity: O(log N)
        return priceToTime.firstKey();
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice obj = new StockPrice();
 * obj.update(timestamp,price);
 * int param_2 = obj.current();
 * int param_3 = obj.maximum();
 * int param_4 = obj.minimum();
 */
