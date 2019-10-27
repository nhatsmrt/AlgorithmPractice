/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     public NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     public NestedInteger(int value);
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public void add(NestedInteger ni);
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
class Solution {
    public int depthSumInverse(List<NestedInteger> nestedList) {
        List<List<Integer>> levels = new ArrayList<List<Integer>>();
        levels.add(new ArrayList<Integer>());

        for (NestedInteger next : nestedList) {
            if (next.isInteger())
                levels.get(0).add(next.getInteger());
        }

        int curLevel = 0;
        if (levels.size() == 1)
            curLevel += 1;
        for (NestedInteger next : nestedList) {
            if (!next.isInteger())
                unroll(next, levels, curLevel);
        }

        int ret = 0;
        for (int i = 0; i < levels.size(); i++) {
            List<Integer> level = levels.get(i);
            for (Integer num : level)
                ret += (levels.size() - i) * num;
        }

        return ret;
    }

    private void unroll(NestedInteger nest, List<List<Integer>> levels, int curLevel) {
        if (curLevel == levels.size())
            levels.add(new ArrayList<Integer>());

        if (nest.isInteger()) {
            int num = nest.getInteger();
            levels.get(curLevel).add(num);
        }
        else {
            List<NestedInteger> nestedList = nest.getList();
            for (NestedInteger next : nestedList) {
                if (next.isInteger())
                    levels.get(curLevel).add(next.getInteger());
            }

            for (NestedInteger next : nestedList) {
                if (!next.isInteger())
                    unroll(next, levels, curLevel + 1);
            }
        }
    }
}
