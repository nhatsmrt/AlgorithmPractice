/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode constructFromPrePost(int[] pre, int[] post) {
        Queue<Integer> preorderQ = new LinkedList<Integer>();
        Stack<Integer> postorderS = new Stack<Integer>();

        for (int i = 0; i < pre.length; i++) {
            preorderQ.add(pre[i]);
            postorderS.push(post[i]);
        }

        return constructFromPrePost(preorderQ, postorderS);
    }

    private TreeNode constructFromPrePost(Queue<Integer> pre, Stack<Integer> post) {
        if (pre.isEmpty())
            return null;




        TreeNode root = new TreeNode(pre.remove());
        post.pop();

        if (!pre.isEmpty()) {
            Stack<Integer> postRight = new Stack<Integer>();
            while (pre.peek() != post.peek())
            postRight.push(post.pop());
            reverse(postRight);

            Queue<Integer> preLeft = new LinkedList<Integer>();
            for (int i = 0; i < post.size(); i++)
                preLeft.add(pre.remove());

            root.left = constructFromPrePost(preLeft, post);
            root.right = constructFromPrePost(pre, postRight);
        }

        return root;
    }

    private void q2s(Queue<Integer> q, Stack<Integer> s) {
        while (!q.isEmpty())
            s.push(q.remove());
    }

    private void s2q(Stack<Integer> s, Queue<Integer> q) {
        while (!s.isEmpty())
            q.add(s.pop());
    }

    private void reverse(Stack<Integer> s) {
        Queue<Integer> tmp = new LinkedList<Integer>();
        s2q(s, tmp);
        q2s(tmp, s);
    }

}
