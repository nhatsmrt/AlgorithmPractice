class SegTreeNode {
    private int start;
    private int end;
    private int sum;
    private SegTreeNode left;
    private SegTreeNode right;

    public SegTreeNode(int start, int end) {
        this.start = start;
        this.end = end;
    }

    public void setLeft(SegTreeNode node) {
        left = node;
    }

    public void setRight(SegTreeNode node) {
        right = node;
    }

    public void setSum(int val) {
        sum = val;
    }

    public SegTreeNode getLeft() {
        return left;
    }

    public SegTreeNode getRight() {
        return right;
    }

    public int getSum() {
        return sum;
    }
}

class NumArray {
    SegTreeNode root;
    int size;

    public NumArray(int[] nums) {
        size = nums.length;
        root = new SegTreeNode(0, size - 1);

        if (size > 0)
            build(nums, root, 0, size - 1);
    }

    public void update(int i, int val) {
        updateTree(i, root, 0, size - 1, val);
    }

    public int sumRange(int i, int j) {
        return sumTree(root, i, j, 0, size - 1);
    }

    // Build the segment tree:
    public void build(int[] nums, SegTreeNode node, int start, int end) {
        if (start == end) {
            node.setSum(nums[start]);
        }
        else {
            int mid = (start + end) / 2;
            SegTreeNode leftNode = new SegTreeNode(start, mid);
            SegTreeNode rightNode = new SegTreeNode(mid + 1, end);

            build(nums, leftNode, start, mid);
            build(nums, rightNode, mid + 1, end);

            node.setSum(leftNode.getSum() + rightNode.getSum());
            node.setLeft(leftNode);
            node.setRight(rightNode);
        }
    }

    public void updateTree(int i, SegTreeNode node, int start, int end, int val) {
        if (start == end) {
            node.setSum(val);
        }
        else {
            int mid = (start + end) / 2;

            if (start <= i && i <= mid)
                updateTree(i, node.getLeft(), start, mid, val);
            else
                updateTree(i, node.getRight(), mid + 1, end, val);

            node.setSum(node.getLeft().getSum() + node.getRight().getSum());
        }
    }

    public int sumTree(SegTreeNode node, int i, int j, int start, int end) {
        // Out of range:
        if (j < start || i > end)
            return 0;

        //  range of node lies in [i, j]
        if (i <= start && end <= j)
            return node.getSum();

        int mid = (start + end) / 2;
        return sumTree(node.getLeft(), i, j, start, mid) + sumTree(node.getRight(), i, j, mid + 1, end);
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */
