/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class NestedIterator implements Iterator<Integer> {
    private Deque<Integer> data;

    public NestedIterator(List<NestedInteger> nestedList) {
        data = new LinkedList<Integer>();
        for (NestedInteger nest : nestedList) {
            if (nest.isInteger())
                data.addLast(nest.getInteger());
            else {
                NestedIterator iterator = new NestedIterator(nest.getList());
                while (iterator.hasNext())
                    data.addLast(iterator.next());
            }
        }
    }

    @Override
    public Integer next() {
        return data.removeFirst();
    }

    @Override
    public boolean hasNext() {
        return !data.isEmpty();
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */
