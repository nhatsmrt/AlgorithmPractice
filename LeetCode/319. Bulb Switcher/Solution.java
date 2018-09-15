class Solution {
    public int bulbSwitch(int n) {
        int ret = 0;
        int cnt = 1;
        while (cnt * cnt <= n) {
            ret += 1;
            cnt += 1;
        }
        return ret;
    }
}
