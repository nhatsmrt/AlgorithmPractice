class MovingAverage {
    private int[] value;
    private int numAdded;
    private int sum;

    /** Initialize your data structure here. */
    public MovingAverage(int size) {
        value = new int[size];
    }

    public double next(int val) {
        if (numAdded < value.length) {
            sum += val;
            value[numAdded] = val;
            numAdded += 1;
            return ((double) sum) / numAdded;
        }
        else {
            int replaceInd = numAdded % value.length;
            sum += val - value[replaceInd];
            value[replaceInd] = val;
            numAdded += 1;
            return ((double) sum) / value.length;
        }
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */
