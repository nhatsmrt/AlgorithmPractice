class Solution {
    int[] furthest;
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int size = nums.length;
        furthest = new int[size];

        int curProd = nums[0];
        furthest[0] = 0;
        int ret = 0;

        for (int i = 0; i < size; i++) {
            int oldVal = i > 0 ? furthest[i - 1] : 0;
            if (i > 0) {
                if (furthest[i - 1] < i) {
                    curProd = nums[i];
                    furthest[i] = i;
                }
                else {
                    curProd /= nums[i - 1];
                    furthest[i] = oldVal;
                }
            }

            while (curProd < k) {
                furthest[i] += 1;
                if (furthest[i] < size)
                    curProd *= nums[furthest[i]];
                else
                    break;
            }


            if (furthest[i] > oldVal) {
                if (furthest[i] < size)
                    curProd /= nums[furthest[i]];

                furthest[i] -= 1;
            }

            if (furthest[i] >= i && curProd < k) {
                ret += (furthest[i] - i + 1);
            }

        }

        return ret;

    }
}
