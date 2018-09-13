class BST {
    private BSTNode root;

    public BST() {}

    public BSTNode insert(int val) {
        if (root == null) {
            root = new BSTNode(val, 0);
            return root;
        }

        return insertRecursive(root, val, 0);
    }

    public BSTNode insertRecursive(BSTNode node, int val, int numLeftCount) {
        if (node == null) {
            node = new BSTNode(val, 0);
            node.setNumLeftAll(numLeftCount);
            return node;
        }

        if (node.getVal() < val) {
            BSTNode ret = insertRecursive(node.getRight(), val, numLeftCount + 1 + node.getNumLeft());
            if (node.getRight() == null)
                node.setRight(ret);
            return ret;
        }
        else if (node.getVal() > val) {
            node.setNumLeft(node.getNumLeft() + 1);
            node.setNumLeftAll(node.getNumLeftAll() + 1);
            BSTNode ret = insertRecursive(node.getLeft(), val, numLeftCount);
            if (node.getLeft() == null)
                node.setLeft(ret);

            return ret;
        }

        BSTNode ret = insertRecursive(node.getRight(), val, node.getNumLeft() + numLeftCount);
        if (node.getRight() == null)
            node.setRight(ret);
        return ret;
    }


}

class BSTNode {
    private int val;
    private BSTNode left;
    private BSTNode right;
    private int numLeft;
    private int numLeftAll;

    public BSTNode() {}

    public BSTNode(int val, int numLeft) {
        this.val = val;
        this.numLeft = numLeft;
    }

    public int getVal() {
        return val;
    }

    public int getNumLeft() {
        return numLeft;
    }

    public int getNumLeftAll() {
        return numLeftAll;
    }

    public BSTNode getLeft() {
        return left;
    }

    public BSTNode getRight() {
        return right;
    }

    public void setNumLeft(int numLeft) {
        this.numLeft = numLeft;
    }

    public void setLeft(BSTNode node) {
        left = node;
    }

    public void setRight(BSTNode node) {
        right = node;
    }

    public void setNumLeftAll(int numLeftAll) {
        this.numLeftAll = numLeftAll;
    }

}


class Solution {
    public List<Integer> countSmaller(int[] nums) {
        ArrayList<Integer> countSmallerList = new ArrayList<Integer>();
        int size = nums.length;
        BST tree = new BST();

        for (int i = size - 1; i >= 0; i--) {
            BSTNode node = tree.insert(nums[i]);
            countSmallerList.add(0, node.getNumLeftAll());
        }

        return countSmallerList;
    }
}
