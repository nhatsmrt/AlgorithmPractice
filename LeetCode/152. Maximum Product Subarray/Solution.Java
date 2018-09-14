class SegTree {
    int MAXINT = 2147483647;

    SegTreeNode root;
    int size;

    public SegTree(int[] nums) {
        size = nums.length;

        if (size > 0) {
            root = new SegTreeNode(0, size - 1);
            build(nums, root, 0, size - 1);
        }
    }

    public void build(int[] nums, SegTreeNode node, int start, int end) {
        // Leaf:
        if (start == end) {
            node.prod = node.maxPrefixProd = node.maxSuffixProd = node.maxSubArrayProd = node.minPrefixProd = node.minSuffixProd = nums[start];
        }
        else {
            int mid = (start + end) / 2;
            node.left = new SegTreeNode(start, mid);
            node.right = new SegTreeNode(mid + 1, end);

            build(nums, node.left, start, mid);
            build(nums, node.right, mid + 1, end);

            node.prod = node.left.prod * node.right.prod;

            node.maxPrefixProd = max4(
                node.prod,
                node.left.maxPrefixProd,
                node.left.prod * node.right.maxPrefixProd,
                node.left.prod * node.right.minPrefixProd
            );

            node.maxSuffixProd = max4(
                node.prod,
                node.right.maxSuffixProd,
                node.right.prod * node.left.maxSuffixProd,
                node.right.prod * node.left.minSuffixProd
            );

            node.minPrefixProd = -max4(
                -node.prod,
                -node.left.minPrefixProd,
                -node.left.prod * node.right.maxPrefixProd,
                -node.left.prod * node.right.minPrefixProd
            );

            node.minSuffixProd = -max4(
                -node.prod,
                -node.right.minSuffixProd,
                -node.right.prod * node.left.maxSuffixProd,
                -node.right.prod * node.left.minSuffixProd
            );

            int maxMid = max4(
                node.left.maxSuffixProd * node.right.maxPrefixProd,
                node.left.minSuffixProd * node.right.minPrefixProd,
                node.left.maxSuffixProd,
                node.right.maxPrefixProd
            );


            node.maxSubArrayProd = max4(node.prod, node.left.maxSubArrayProd, node.right.maxSubArrayProd, maxMid);

        }
    }

    public int max3(int a, int b, int c) {
        if (a >= b && a >= c)
            return a;
        else if (b >= a && b >= c)
            return b;

        return c;
    }

    public int max4(int a, int b, int c, int d) {
        if (a >= b && a >= c & a >= d)
            return a;
        else if (b >= a && b >= c & b >= d)
            return b;
        else if (c >= a && c >= b && c >= d)
            return c;

        return d;
    }

    public int max5(int a, int b, int c, int d, int e) {
        if (a >= b && a >= c & a >= d & a >= e)
            return a;
        else if (b >= a && b >= c & b >= d & b >= e)
            return b;
        else if (c >= a && c >= b && c >= d && c >= e)
            return c;
        else if (d >= a && d >= b && d >= c && d >= e)
            return d;

        return e;
    }



    public int maxRange() {
        return root.maxSubArrayProd;
    }

    class SegTreeNode {
        int prod;
        int maxPrefixProd;
        int maxSuffixProd;
        int minPrefixProd;
        int minSuffixProd;
        int maxSubArrayProd;
        int start;
        int end;
        SegTreeNode left;
        SegTreeNode right;

        public SegTreeNode(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }
}
class Solution {
    public int maxProduct(int[] nums) {
        SegTree tree = new SegTree(nums);
        return tree.maxRange();
    }
}
