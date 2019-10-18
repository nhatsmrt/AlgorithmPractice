class Solution {
    public String nextClosestTime(String time) {
        Set<Character> digits = new HashSet<Character>();
        for (int i = 0; i < time.length(); i++) {
            if (time.charAt(i) != ':')
                digits.add(time.charAt(i));
        }

        int curMin = -1;
        String ret = "";
        int[] parts = toParts(time);
        int mins = toMins(parts);

        for (Character c1 : digits) {
            for (Character c2 : digits) {
                for (Character c3 : digits) {
                    for (Character c4 : digits) {
                        StringBuilder builder = new StringBuilder();
                        builder.append(c1);
                        builder.append(c2);
                        builder.append(':');
                        builder.append(c3);
                        builder.append(c4);
                        String candidate = builder.toString();
                        int[] candidateParts = toParts(candidate);
                        if (isValid(candidateParts)) {
                            int candidateMins = toMins(candidateParts);
                            int diff = difference(mins, candidateMins);
                            if (curMin == -1 || curMin > diff) {
                                curMin = diff;
                                ret = candidate;
                            }
                        }

                    }
                }
            }
        }

        return ret;
    }

    private int difference(int min1, int min2) {
        if (min2 > min1)
            return min2 - min1;
        else
            return min2 + 24 * 60 - min1;
    }

    private boolean isValid(int[] parts) {
        int hour = parts[0];
        int min = parts[1];

        return 0 <= hour && hour < 24 && 0 <= min && min < 60;
    }

    private int[] toParts (String time) {
        int[] ret = new int[2];
        String[] parts = time.split(":");
        ret[0] = new Integer(parts[0]);
        ret[1] = new Integer(parts[1]);

        return ret;
    }

    private int toMins(int[] parts) {
        int hour = parts[0];
        int min = parts[1];
        return 60 * hour + min;
    }
}
