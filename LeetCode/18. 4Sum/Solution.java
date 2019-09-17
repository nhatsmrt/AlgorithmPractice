class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Map<Integer, List<List<Integer>>> map = new HashMap<Integer, List<List<Integer>>>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                int sum = nums[i] + nums[j];
                List<Integer> list = new ArrayList<Integer>();
                list.add(i);
                list.add(j);

                if (!map.containsKey(sum))
                    map.put(sum, new ArrayList<List<Integer>>());
                map.get(sum).add(list);
            }
        }

        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        Set<String> codes = new HashSet<String>();

        for (Integer first : map.keySet()) {
            int second = target - first;
            if (map.containsKey(second)) {
                for (List<Integer> half1 : map.get(first)) {
                    for (List<Integer> half2 : map.get(second)) {
                        if (half2.get(0) > half1.get(1)) {
                            String code = nums[half1.get(0)] + "_" + nums[half1.get(1)] + "_" +  nums[half2.get(0)] + "_" + nums[half2.get(1)];
                            if (!codes.contains(code)) {
                                List<Integer> list = new ArrayList<Integer>();
                                list.add(nums[half1.get(0)]);
                                list.add(nums[half1.get(1)]);
                                list.add(nums[half2.get(0)]);
                                list.add(nums[half2.get(1)]);
                                ret.add(list);
                                codes.add(code);
                            }
                        }
                    }
                }
            }
        }

        return ret;
    }
}
