class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        int i = 0;
        int j = 0;
        Stack<Integer> s = new Stack<Integer>();

        while (i < pushed.length && j < popped.length) {

            if (pushed[i] != popped[j])
                s.push(pushed[i]);
            else {
                j += 1;
                while (j < popped.length && !s.isEmpty() && s.peek() == popped[j]) {
                    s.pop();
                    j += 1;
                }
            }
            i += 1;
        }

        while (j < popped.length && !s.isEmpty() && s.peek() == popped[j]) {
            s.pop();
            j += 1;
        }


        return j == popped.length;
    }
}
