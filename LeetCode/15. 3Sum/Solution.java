class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);

        Map<Integer, List<Integer>> map = new HashMap<Integer, List<Integer>>();
        for (int i = 0; i < nums.length; i++) {
            if (!map.containsKey(nums[i]))
                map.put(nums[i], new ArrayList<Integer>());
            map.get(nums[i]).add(i);
        }

        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            for (int j = i + 1; j < nums.length; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1])
                    continue;

                if (map.containsKey(-nums[i] - nums[j])) {
                    List<Integer> candidates = map.get(-nums[i] - nums[j]);
                    for (int k = 0; k < candidates.size(); k++) {
                        if (candidates.get(k) > j) {
                            List<Integer> sol = new ArrayList<Integer>();
                            sol.add(nums[i]);
                            sol.add(nums[j]);
                            sol.add(nums[candidates.get(k)]);

                            ret.add(sol);
                            break;
                        }
                    }
                }
            }
        }

        return ret;
    }
}
