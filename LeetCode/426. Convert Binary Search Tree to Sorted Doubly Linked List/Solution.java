/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/
class Solution {


    public Node treeToDoublyList(Node root) {
        if (root == null)
            return null;

        return toList(root).front;
    }

    private DoublyList toList(Node root) {
        if (root == null)
            return null;

        DoublyList leftList = toList(root.left);
        DoublyList rightList = toList(root.right);

        if (leftList == null)
            leftList = new DoublyList(root);
        else {
            leftList.front.left = root;
            leftList.rear.right = root;
            root.left = leftList.rear;
            root.right = leftList.front;
            leftList.rear = root;
        }

        if (rightList != null) {
            leftList.rear.right = rightList.front;
            rightList.front.left = leftList.rear;
            leftList.front.left = rightList.rear;
            rightList.rear.right = leftList.front;
            leftList.rear = rightList.rear;
        }

        return leftList;
    }

    private class DoublyList {
        Node front;
        Node rear;

        public DoublyList(Node root) {
            front = rear = root;
            root.right = root.left = root;
        }
    }
}
