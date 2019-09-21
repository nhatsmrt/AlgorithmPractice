class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        List<Integer> ret = new ArrayList<Integer>();
        int insertionPoint = Arrays.binarySearch(arr, x);
        if (insertionPoint < 0)
            insertionPoint = -insertionPoint - 1;

        int i = insertionPoint;
        int j = insertionPoint - 1;
        int numPicked = 0;

        while (numPicked < k) {
            if (i >= arr.length)
                j -= 1;
            else if (j < 0)
                i += 1;
            else {
                if (Math.abs(x - arr[i]) < Math.abs(x - arr[j]))
                    i += 1;
                else
                    j -= 1;
            }
            numPicked += 1;
        }

        for (int m = j + 1; m <= i - 1; m++)
            ret.add(arr[m]);

        return ret;
    }
}
