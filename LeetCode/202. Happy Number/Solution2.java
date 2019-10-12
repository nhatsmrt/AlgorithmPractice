class Solution {
    public boolean isHappy(int n) {
        if (n == 1)
            return true;
        Set<Integer> nums = new HashSet<Integer>();

        do {
            nums.add(n);
            n = transform(n);
            if (n == 1)
                return true;
        } while(!nums.contains(n));

        return false;
    }

    private int transform(int n) {
        int ret = 0;
        while (n > 0) {
            int dig = n % 10;
            n /= 10;
            ret += dig * dig;
        }

        return ret;
    }
}
