class Solution {
    Map<String, List<String>> dpMap;
    public List<String> removeInvalidParentheses(String s) {
        dpMap = new HashMap<String, List<String>>();
        int curMax = 0;
        Set<String> ret = new HashSet<String>();
        List<List<String>> candidates = new ArrayList<List<String>>();

        for (int i = s.length() - 1; i >= 0; i--) {
            List<String> candidate = longestFrom(s, i, 0);
            if (candidate.size() > 0) {
                if (candidate.get(0).length() > curMax)
                    curMax = candidate.get(0).length();
            }
            candidates.add(candidate);
        }

        if (curMax == 0) {
            ret.add("");
            return new ArrayList<String>(ret);
        }

        for (List<String> candidate : candidates) {
            if (candidate.get(0).length() == curMax)
                ret.addAll(candidate);
        }

        return new ArrayList<String>(ret);
    }

    private List<String> longestFrom(String s, int i, int numOpen) {
        String key = i + "_" + numOpen;

        if (dpMap.containsKey(key))
            return dpMap.get(key);

        List<String> ret = new ArrayList<String>();
        if (i == s.length()) {
            if (numOpen > 0)
                return ret;
            else {
                ret.add("");
                return ret;
            }
        }
        else {
            if (s.charAt(i) == '(') {
                List<String> candidate1 = longestFrom(s, i + 1, numOpen + 1);
                List<String> candidate2 = longestFrom(s, i + 1, numOpen);

                if (candidate1.size() != 0 || candidate2.size() != 0) {
                    if (candidate1.size() == 0)
                        ret.addAll(candidate2);
                    else if (candidate2.size() == 0) {
                        for (String str : candidate1)
                            ret.add("(" + str);
                    }
                    else {
                        if (candidate1.get(0).length() + 1 > candidate2.get(0).length()) {
                            for (String str : candidate1)
                                ret.add("(" + str);
                        }
                        else if (candidate2.get(0).length() > candidate1.get(0).length() + 1) {
                            for (String str : candidate2)
                                ret.add(str);
                        }
                        else {
                            for (String str : candidate1)
                                ret.add("(" + str);

                            for (String str : candidate2)
                                ret.add(str);
                        }
                    }
                }
            }
            else if (s.charAt(i) == ')') {
                if (numOpen == 0)
                    ret = longestFrom(s, i + 1, numOpen);
                else {
                    List<String> candidate1 = longestFrom(s, i + 1, numOpen - 1);
                    List<String> candidate2 = longestFrom(s, i + 1, numOpen);

                    if (candidate1.size() != 0 || candidate2.size() != 0) {
                        if (candidate1.size() == 0)
                            ret.addAll(candidate2);
                        else if (candidate2.size() == 0) {
                            for (String str : candidate1)
                                ret.add(")" + str);
                        }
                        else {
                            if (candidate1.get(0).length() + 1 > candidate2.get(0).length()) {
                                for (String str : candidate1)
                                    ret.add(")" + str);
                            }
                            else if (candidate2.get(0).length() > candidate1.get(0).length() + 1) {
                                for (String str : candidate2)
                                    ret.add(str);
                            }
                            else {
                                for (String str : candidate1)
                                    ret.add(")" + str);

                                for (String str : candidate2)
                                    ret.add(str);
                            }
                        }
                    }
                }
            }
            else {
                List<String> candidate = longestFrom(s, i + 1, numOpen);
                for (String str : candidate)
                    ret.add(s.charAt(i) + str);
            }
        }

        dpMap.put(key, ret);
        return ret;
    }
}
