class Solution {
    private Map <String, Boolean> dpMap;

    public boolean isMatch(String s, String p) {
        dpMap = new HashMap<String, Boolean>();
        return isMatchDP(s, p);
    }

    private boolean isMatchDP(String s, String p) {
        int strLen = s.length();
        int patLen = p.length();

        String key = s + "_" + p;
        boolean ret;

        if (dpMap.containsKey(key))
            return dpMap.get(key);

        if (patLen == 0 && strLen == 0)
            return true;

        if (patLen == 0 && strLen != 0)
            return false;

        if (strLen == 0) {
            if (patLen >= 2 && p.charAt(1) == '*')
                ret = isMatchDP(s, p.substring(2));
            else
                ret = false;

            dpMap.put(key, ret);
            return ret;
        }

        if (patLen == 1) {
            if (p.charAt(0) == '.')
                return strLen == 1;
            else if (p.charAt(0) == '*') {
                for (int i = 1; i < strLen; i++) {
                    if (s.charAt(i) != s.charAt(0)) {
                        dpMap.put(key, false);
                        return false;
                    }
                }
                dpMap.put(key, true);
                return true;
            }
            else {
                ret = strLen == 1 && s.charAt(0) == p.charAt(0);
                dpMap.put(key, ret);
                return ret;
            }
        }

        if (p.charAt(1) == '*') {
            if (p.charAt(0) == '.')
                ret = isMatchDP(s, p.substring(2)) || isMatchDP(s.substring(1), p);
            else {
                if (s.charAt(0) == p.charAt(0))
                    ret = isMatchDP(s, p.substring(2)) || isMatchDP(s.substring(1), p);
                else
                    ret = isMatchDP(s, p.substring(2));
            }
        }
        else {
            if (p.charAt(0) == '.')
                ret =  isMatchDP(s.substring(1), p.substring(1));
            else {
                if (s.charAt(0) != p.charAt(0))
                    ret = false;
                else
                    ret = isMatchDP(s.substring(1), p.substring(1));
            }
        }

        dpMap.put(key, ret);
        return ret;
    }
}
