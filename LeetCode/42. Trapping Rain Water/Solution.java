class Solution {
    public int trap(int[] height) {
        int ret = 0;
        int begin = 0;
        int finalPoint = height.length - 1;

        while (finalPoint > 0 && height[finalPoint] == 0)
            finalPoint -= 1;
        if (finalPoint == 0)
            return 0;

        while (begin < height.length && height[begin] == 0)
            begin += 1;
        if (begin == height.length)
            return 0;

        int end = 0;
        while (begin <= finalPoint - 2) {
            end = begin;
            int curMax = height[begin + 1];
            do {
                end += 1;
                if (end <= finalPoint && height[end] >= curMax)
                    curMax = height[end];
            } while (end <= finalPoint && height[end] < height[begin]);

            if (end == begin + 1) {
                begin += 1;
            }
            else if (end == finalPoint + 1) {
                height[begin] = curMax;
            }
            else {
                int waterLevel = height[begin];
                for (int i = begin; i < end; i++) {
                    ret += waterLevel - height[i];
                }
                begin = end;
            }
        }

        return ret;
    }
}
