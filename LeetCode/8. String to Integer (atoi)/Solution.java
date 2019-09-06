class Solution {
    public int myAtoi(String str) {
        int MAX = 2147483647;
        int i = 0;
        boolean started = false;
        boolean foundSign = false;
        boolean pos = true;

        int ret = 0;
        while (i < str.length()) {
            if (str.charAt(i) != ' ') {
                if (str.charAt(i) == '+' || str.charAt(i) == '-') {
                    if (foundSign || started)
                        break;
                    else {
                        pos = str.charAt(i) == '+';
                        foundSign = true;
                        started = true;
                    }
                }
                else if (str.charAt(i) >= '0' && str.charAt(i) <= '9') {
                    started = true;
                    int candidate = ret * 10 + (str.charAt(i) - '0');
                    if (candidate / 10 != ret) {
                        if (pos)
                            return MAX;
                        else
                            return -MAX - 1;
                    }
                    else
                        ret = candidate;
                }
                else
                    break;
            }
            else {
                if (started)
                    break;
            }
            i += 1;
        }

        if (pos)
            return ret;
        else
            return -ret;
    }

}
