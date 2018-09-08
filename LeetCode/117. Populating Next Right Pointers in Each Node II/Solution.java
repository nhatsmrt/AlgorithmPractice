/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    private ArrayDeque<TreeLinkNode> deque = new ArrayDeque<TreeLinkNode>();
    private void connectNode(TreeLinkNode node, TreeLinkNode parent) {
        if (parent.right != null && parent.right != node)
                node.next = parent.right;
        else {
            TreeLinkNode uncle = parent.next;
            while (uncle != null) {
                if (uncle.left != null && uncle.left != node) {
                    node.next = uncle.left;
                    return;
                }
                else if (uncle.right != null && uncle.right != node) {
                    node.next = uncle.right;
                    return;
                }
                else
                    uncle = uncle.next;
            }
        }

    }
    public void connect(TreeLinkNode root) {
        if (root == null)
            return;

        deque.addFirst(root);
        if (root.left != null)
            deque.addLast(root.left);
        else if (root.right != null)
            deque.addLast(root.right);
        else {
            return;
        }

        while (deque.size() == 2) {
            TreeLinkNode parNode = deque.removeFirst();
            TreeLinkNode childNode = deque.peekFirst();
            TreeLinkNode it = childNode;
            TreeLinkNode itPar = parNode;

            // connect all node in child's level:
            int counter = 0;
            do {
                // Find the correct parent:
                while(
                    (parNode.left == null || (parNode.left != null && parNode.left != it)) &&
                    (parNode.right == null || (parNode.right != null && parNode.right != it))
                )
                    parNode = parNode.next;

                itPar = parNode;
                connectNode(it, itPar);
                it = it.next;
                counter += 1;
                if (counter > 1024) {
                    System.out.println("error here");
                    break;
                }
            } while (it != null);

            // add the first grandchild:
            it = childNode;
            counter = 0;
            while (it != null) {
                if (it.left != null) {
                    deque.addLast(it.left);
                    break;
                }
                else if (it.right != null) {
                    deque.addLast(it.right);
                    break;
                }
                else {
                    deque.removeFirst();
                    it = it.next;
                    if (it != null)
                        deque.addFirst(it);
                }
                counter += 1;
                if (counter > 1024) {
                    System.out.println("error here");
                    break;
                }
            }

            if (it == null)
                return;
        }


    }
}
