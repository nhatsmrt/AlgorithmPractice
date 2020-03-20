class NumArray {
    // Fenwick Tree
    private int[] data;

    public NumArray(int[] nums) {
        data = new int[nums.length + 1];
        // data[i] = sum_{j = (i - 1) - 1 << r}^{i - 1} nums[j]
        // where r is the last set bit of i - 1
        // (for simplicity, data is defined with starting index 1)
        int[] prefixes = new int[nums.length + 1];

        for (int i = 1; i < nums.length + 1; i++) {
            prefixes[i] = prefixes[i - 1] + nums[i - 1];
            data[i] = prefixes[i] - prefixes[i - lastSetBit(i)];
        }
    }

    public void update(int i, int val) {
        int oldValue = prefix(i + 1) - prefix(i);
        add(i + 1, val - oldValue);
    }

    public int sumRange(int i, int j) {
        return prefix(j + 1) - prefix(i);
    }

    private void add(int index, int val) {
        while (index < data.length) {
            data[index] += val;
            index += lastSetBit(index);
        }
    }

    private int prefix(int index) {
        int ret = 0;
        while (index > 0) {
            ret += data[index];
            index -= lastSetBit(index);
        }

        return ret;
    }

    private int lastSetBit(int ind) {
        return ind & (-ind);
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */
