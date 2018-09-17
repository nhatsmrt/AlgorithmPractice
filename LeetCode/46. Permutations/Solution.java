class Solution {
    public boolean accept(int[] nums, List<Integer> permutation) {
        Set<Integer> sizeCheckSet = new HashSet<Integer>(permutation);

        if (sizeCheckSet.size() == nums.length)
            return true;

        return false;
    }

    public boolean reject(List<Integer> permutation) {
        Set<Integer> sizeCheckSet = new HashSet<Integer>(permutation);

        if (sizeCheckSet.size() < permutation.size())
            return true;

        return false;
    }


    public List<Integer> extend(int[] nums, List<Integer> permutation) {
        List<Integer> newPermutation = new ArrayList<Integer>(permutation);
        newPermutation.add(nums[0]);
        return newPermutation;
    }

    public List<Integer> next(int[] nums, List<Integer> permutation) {
        Integer lastAdded = permutation.get(permutation.size() - 1);
        List<Integer> newPermutation = new ArrayList<Integer>(permutation);
        newPermutation.remove(permutation.size() - 1);

        for (int i = 0; i < nums.length - 1; i++) {
            if (lastAdded == nums[i]) {
                newPermutation.add(nums[i + 1]);
                break;
            }

        }

        return newPermutation;
    }

    public void backtrack(int[] nums, List<Integer> permutation, List<List<Integer>> permutations) {
        if (reject(permutation))
            return;

        if (accept(nums, permutation)) {
            permutations.add(permutation);
            return;
        }

        List<Integer> extendedPermutation = extend(nums, permutation);

        for (int i = 0; i < nums.length; i++) {
            backtrack(nums, extendedPermutation, permutations);
            extendedPermutation = next(nums, extendedPermutation);
        }

    }
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> permutations = new ArrayList<List<Integer>>();
        List<Integer> root = new ArrayList<Integer>();
        backtrack(nums, root, permutations);
        return permutations;
    }
}
