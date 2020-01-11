/* Hidden stub code will pass a root argument to the function below. Complete the function to solve the challenge. Hint: you may want to write one or more helper functions.

The Node class is defined as follows:
    class Node {
        int data;
        Node left;
        Node right;
     }
*/
    boolean checkBST(Node root) {
        return check(root, -1, 10001);
    }

    boolean check(Node node, int lower, int upper) {
        if (node == null)
            return true;

        if (node.data <= lower || node.data >= upper)
            return false;

        return check(node.left, lower, node.data) && check(node.right, node.data, upper);
    }
