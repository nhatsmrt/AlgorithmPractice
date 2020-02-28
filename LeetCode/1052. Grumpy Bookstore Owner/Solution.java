class Solution {
    public int maxSatisfied(int[] customers, int[] grumpy, int X) {
        int happy = 0;
        for (int i = 0; i < customers.length; i++)
            happy += customers[i] * (1 - grumpy[i]);

        int maxHappified;
        int windowHappified = 0;

        for (int i = 0; i < X; i++)
            windowHappified += customers[i] * grumpy[i];

        maxHappified = windowHappified;

        for (int i = X; i < customers.length; i++) {
            windowHappified += grumpy[i] * customers[i] - grumpy[i - X] * customers[i - X];
            maxHappified = Math.max(maxHappified, windowHappified);
        }

        return happy + maxHappified;
    }
}
