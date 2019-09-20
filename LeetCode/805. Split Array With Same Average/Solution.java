class Solution {
    private Map<Long, Double> dp;
    private TreeMap<Double, List<Long>> reverseMap;
    private long maxMask;

    public boolean splitArraySameAverage(int[] A) {
        if (A.length == 1)
            return false;
        if (A.length == 2)
            return A[0] == A[1];

        int sum = 0;
        for (int num : A)
            sum += num;

        double avg = ((double) sum) / A.length;
        double[] nums = new double[A.length];
        for (int i = 0; i < A.length; i++)
            nums[i] = (double) A[i] - avg;

        dp = new HashMap<Long, Double>();


        maxMask = (1 << (A.length)) - 1;
        long maxMaskLeft = (1 << (A.length / 2)) - 1;
        long maxMaskRight = (1 << (A.length - A.length / 2)) - 1;
        reverseMap = new TreeMap<Double, List<Long>>();

        for (long i = 1; i <= maxMaskLeft; i++) {
            double candidate = findSum(i, nums);
            if (isZero(candidate)) {
                return true;
            }
            if(!reverseMap.containsKey(candidate))
                reverseMap.put(candidate, new ArrayList<Long>());
            reverseMap.get(candidate).add(i);
        }

        for (long i = 1; i <= maxMaskRight; i++) {
            long mask = i << A.length / 2;
            double candidate = findSum(mask, nums);

            try {
                double key = reverseMap.floorKey(-candidate);
                if (isZero(key + candidate)) {
                    if (reverseMap.get(key).size() > 1)
                        return true;
                    else if (reverseMap.get(key).get(0) + mask < maxMask)
                        return true;
                }

                key = reverseMap.ceilingKey(-candidate);
                if (isZero(key + candidate)) {
                    if (reverseMap.get(key).size() > 1)
                        return true;
                    else if (reverseMap.get(key).get(0) + mask < maxMask)
                        return true;
                }
            } catch(NullPointerException e) {
                continue;
            }
        }

        return false;
    }

    public double findSum(long mask, double[] nums) {
        if (mask == 0)
            return 0;

        if (dp.containsKey(mask))
            return dp.get(mask);

        int i = 0;
        double ret = 0.0;

        int firstElement = Long.numberOfTrailingZeros(mask);
        ret = nums[firstElement] + findSum(mask - (1 << firstElement), nums);

        dp.put(mask, ret);
        dp.put(maxMask - mask, -ret);
        return ret;
    }

    public boolean isZero(double x) {
        return -0.000000001 < x && x < 0.000000001;
    }
}
