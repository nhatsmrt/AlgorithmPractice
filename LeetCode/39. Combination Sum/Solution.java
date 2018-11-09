class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<Integer> candidatesList = new ArrayList<Integer>();
        for (int num : candidates)
            candidatesList.add(num);

        return combinationSum(new ArrayList<Integer>(), candidatesList, target);
    }

    private List<List<Integer>> combinationSum(List<Integer> cur, List<Integer> candidates, int target) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        if (candidates.isEmpty()) { // base case
            if (target == 0)
                ret.add(clone(cur));

            return ret;
        }
        else {
            int candidate = candidates.get(candidates.size() - 1);
            candidates.remove(candidates.size() - 1);
            ret = combinationSum(cur, candidates, target);
            candidates.add(candidate);

            if (candidate <= target) {
                cur.add(candidate);
                ret.addAll(combinationSum(cur, candidates, target - candidate));
                cur.remove(cur.size() - 1);
            }

            return ret;
        }
    }

    private List<Integer> clone(List<Integer> list) {
        return new ArrayList<Integer>(list);
    }
}
