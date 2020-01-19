class Solution {
  public int findPoisonedDuration(int[] timeSeries, int duration) {
      // Adapting Klee's Algorithm
      // Time Complexity: O(n)
      if (timeSeries.length == 0)
        return 0;
      int totalLength = 0;

      // Observation: We don't need to keep track of the counter
      // as the length of the intervals are identical
      // so counter == 0 only when timeSeries[i + 1] > timeSeries[i] + duration
      // in which case the increment is duration; otherwise we can just
      // "skip" the right endpoints and go straight to the next left endpoints
      for(int i = 0; i < timeSeries.length - 1; i++)
        totalLength += Math.min(timeSeries[i + 1] - timeSeries[i], duration);

      // Observation 2: The last interval is left alone
      return totalLength + duration;
  }
}
