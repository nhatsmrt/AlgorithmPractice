class Solution {
    private float[] weights;
    private Random r;

    public Solution(int[] w) {
        weights = new float[w.length];
        weights[0] = w[0];
        for(int i = 1; i < w.length; i++)
            weights[i] = weights[i - 1] + w[i];

        for (int i = 0; i < w.length; i++)
            weights[i] /= weights[weights.length - 1];
        r = new Random();
    }

    public int pickIndex() {
		float num = r.nextFloat();
        int indices = Arrays.binarySearch(weights, num);
        if (indices >= 0)
            return indices;
        else
            return -indices - 1;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */
