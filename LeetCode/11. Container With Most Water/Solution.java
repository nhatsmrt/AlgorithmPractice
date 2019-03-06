class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;

        while (left < right) {
            int cand = Math.min(height[left], height[right]) * (right - left);
            if (cand > maxArea)
                maxArea = cand;
            if (height[left] < height[right])
                left += 1;
            else
                right -= 1;
        }

        return maxArea;
    }
}
