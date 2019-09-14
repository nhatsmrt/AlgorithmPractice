class Solution {
    public int totalFruit(int[] tree) {
        Map<Integer, Integer> multiset = new HashMap<Integer, Integer>();
        int[] numFruits = new int[tree.length];

        int i = 0;
        int j = 0;

        while (i < numFruits.length) {
            if (j < numFruits.length && (multiset.containsKey(tree[j]) || multiset.size() < 2)) {
                if (!multiset.containsKey(tree[j]))
                    multiset.put(tree[j], 1);
                else
                    multiset.put(tree[j], multiset.get(tree[j]) + 1);

                j += 1;
            }
            else {
                numFruits[i] = j - i;

                if (j == numFruits.length)
                    break;

                if (multiset.get(tree[i]) == 1)
                    multiset.remove(tree[i]);
                else
                    multiset.put(tree[i], multiset.get(tree[i]) - 1);
                i += 1;
            }
        }

        int ret = 0;
        for (int k = 0; k < numFruits.length; k++) {
            if (ret < numFruits[k])
                ret = numFruits[k];
        }

        return ret;
    }
}
