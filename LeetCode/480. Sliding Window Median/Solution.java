class SlidingMedian {
    private PriorityQueue<Double> left; // max heap
    private PriorityQueue<Double> right; // min heap
    private Map<Double, Integer> invalids;
    private int difference;
    private int size;

    public SlidingMedian() {
        left = new PriorityQueue<>();
        right = new PriorityQueue<>();
        invalids = new HashMap<>();
    }

    public void add(int value) {
        if (size == 0) {
            left.offer(-(double) value);
            difference += 1;
        }
        else {
            double median = median();
            if (value < median) {
                left.offer(-(double) value);
                difference += 1;
            }
            else {
                right.offer((double) value);
                difference -= 1;
            }

            correct();
        }
        size += 1;
    }

    public void remove(int value) {
        double median = median();
        if (value <= median)
            difference -= 1;
        else
            difference += 1;
        invalids.put((double) value, invalids.getOrDefault((double) value, 0) + 1);
        correct();
        size -= 1;
    }

    public double median() {
        correct();

        if (difference == 0) {
            double first = -left.peek();
            double second = right.peek();

            return ( first + second) / 2;
        }
        else
            return -left.peek();
    }

    private void correct() {
        while (
            difference < 0 || difference > 1 ||
            (!left.isEmpty() && invalids.containsKey(-left.peek())) ||
            (!right.isEmpty() && invalids.containsKey(right.peek()))
        ) {
            if (!left.isEmpty() && invalids.containsKey(-left.peek()))
                removeFromInvalids(-left.poll());

            if (!right.isEmpty() && invalids.containsKey(right.peek()))
                removeFromInvalids(right.poll());
            rebalance();
        }
    }

    private void rebalance() {
        while (difference > 1) {
            double candidate = -left.poll();
            if (!invalids.containsKey(candidate)) {
                right.offer(candidate);
                difference -= 2;
            }
            else
                removeFromInvalids(candidate);
        }

        while (difference < 0) {
            double candidate = right.poll();
            if (!invalids.containsKey(candidate)) {
                left.offer(-candidate);
                difference += 2;
            }
            else
                removeFromInvalids(candidate);
        }
    }

    private void removeFromInvalids(double value) {
        int count = invalids.get(value);
        if (count == 1)
            invalids.remove(value);
        else
            invalids.put(value, count - 1);
    }
}


class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        double[] ret = new double[nums.length - k + 1];
        SlidingMedian sm = new SlidingMedian();

        for (int i = 0; i < k; i++) {
            sm.add(nums[i]);
        }
        ret[0] = sm.median();

        for (int i = 0; i < nums.length - k; i++) {
            sm.remove(nums[i]);
            sm.add(nums[i + k]);
            ret[i + 1] = sm.median();
        }

        return ret;
    }
}
