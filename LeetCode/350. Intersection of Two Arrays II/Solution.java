class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Map<Integer, Integer> num1Set = new HashMap<>();
        for (int num : nums1)
            num1Set.put(num, num1Set.getOrDefault(num, 0) + 1);

        List<Integer> ret = new ArrayList<>();
        for (int num : nums2) {
            if (num1Set.containsKey(num)) {
                int cnt = num1Set.get(num) - 1;
                if (cnt == 0)
                    num1Set.remove(num);
                else
                    num1Set.put(num, cnt);

                ret.add(num);
            }
        }

        int[] retArr = new int[ret.size()];
        for (int i = 0; i < ret.size(); i++)
            retArr[i] = ret.get(i);

        return retArr;
    }
}
