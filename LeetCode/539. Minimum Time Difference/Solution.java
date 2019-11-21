class Solution {
    public int findMinDifference(List<String> timePoints) {
        int[] minutes = new int[timePoints.size()];
        for (int i = 0; i < timePoints.size(); i++)
            minutes[i] = timeToMin(timePoints.get(i));
        countingSort(minutes);

        int ret = -1;
        for (int i = 0; i < minutes.length - 1; i++) {
            int candidate = minutes[i + 1] - minutes[i];
            ret = (ret == - 1  || ret > candidate) ? candidate : ret;
        }

        int candidate = minutes[0] + 24 * 60 - minutes[minutes.length - 1];

        return ret < candidate ? ret : candidate;
    }

    private int timeToMin(String time) {
        int hours = (int)(time.charAt(0) - '0') * 10 + (time.charAt(1) - '0');
        int minutes = (int)(time.charAt(3) - '0') * 10 + (time.charAt(4) - '0');
        return hours * 60 + minutes;
    }

    private void countingSort(int[] minutes) {
        int[] bins = new int[1440];
        for (int minute : minutes)
            bins[minute] += 1;

        int cnt = 0;
        for (int i = 0; i < 1440; i++) {
            for (int j = 0; j < bins[i]; j++) {
                minutes[cnt] = i;
                cnt += 1;
            }
        }
    }
}
