class DynaSegTree {
    private DynaSegTreeNode root;

    public DynaSegTree() {
        root = new DynaSegTreeNode();
        root.start = 0;
        root.end = 1000000000;
        root.max = 0;
    }

    public void add(int L, int R) {
        add(root, L, R);
    }

    private void add(DynaSegTreeNode node, int L, int R) {
        if (node.start <= R && node.end >= L) {
            if (node.start == node.end)
                node.max += 1;
            else if (L <= node.start && node.end <= R)
                node.lazy += 1;
            else {
                int mid = (node.start + node.end) / 2;
                if (node.left == null) {
                    node.left = new DynaSegTreeNode();
                    node.left.start = node.start;
                    node.left.end = mid;
                    node.left.max = 0;
                }

                if (node.right == null) {
                    node.right = new DynaSegTreeNode();
                    node.right.start = mid + 1;
                    node.right.end = node.end;
                    node.right.max = 0;
                }

                node.left.lazy += node.lazy;
                node.right.lazy += node.lazy;
                node.lazy = 0;

                if (L <= mid)
                    add(node.left, L, R);

                if (R >= mid + 1)
                    add(node.right, L, R);

                if (node.left == null)
                    node.max = node.right.max + node.right.lazy;
                else if (node.right == null)
                    node.max = node.left.max + node.left.lazy;
                else {
                    int candidate1 = node.right.max + node.right.lazy;
                    int candidate2 = node.left.max + node.left.lazy;
                    node.max = candidate1 > candidate2 ? candidate1 : candidate2;
                }
            }
        }
    }

    public int max() {
        if (root == null)
            return 0;
        return root.max;
    }

    private class DynaSegTreeNode {
        int start;
        int end;
        int max;
        int lazy;
        DynaSegTreeNode left;
        DynaSegTreeNode right;
    }
}


class MyCalendarThree {
    private DynaSegTree data;

    public MyCalendarThree() {
        data = new DynaSegTree();
    }

    public int book(int start, int end) {
        data.add(start, end - 1);
        return data.max();
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree obj = new MyCalendarThree();
 * int param_1 = obj.book(start,end);
 */
