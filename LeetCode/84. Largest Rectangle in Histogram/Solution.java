class Solution {
    public int largestRectangleArea(int[] heights) {
        if (heights.length == 0)
            return 0;

        int left[] = new int[heights.length];
        int right[] = new int[heights.length];

        left[0] = 0;
        right[heights.length - 1] = heights.length - 1;
        for (int i = 0; i < heights.length; i++) {
            if (i == 0 || heights[i] > heights[i - 1]) {
                left[i] = i;
            }
            else {
                int l = i - 1;
                while (left[l] - 1 >= 0 && heights[i] <= heights[left[l] - 1])
                    l = left[l] - 1;
                left[i] = left[l];
            }
        }

        for (int i = heights.length - 1; i >= 0; i--) {
            if (i == heights.length - 1 || heights[i] > heights[i + 1]) {
                right[i] = i;
            }
            else {
                int r = i + 1;
                while (right[r] + 1 < heights.length && heights[i] <= heights[right[r] + 1])
                    r = right[r] + 1;
                right[i] = right[r];
            }
        }

        // for (int i = 0; i < heights.length; i++)
        //     System.out.println(right[i]);

        int curMax = 0;
        for (int i = 0; i < heights.length; i++) {
            int candidate = heights[i] * (right[i] - left[i] + 1);
            if (candidate > curMax)
                curMax = candidate;
        }

        return curMax;
    }
}
