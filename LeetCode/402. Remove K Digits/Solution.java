class Solution {
    public String removeKdigits(String num, int k) {
        if (k == num.length())
            return "0";

        int numDeleted = 0;
        Stack<Character> stack = new Stack<Character>();
        for (int i = 0; i < num.length(); i++) {
            while (numDeleted < k && !stack.isEmpty() && stack.peek() > num.charAt(i)) {
                stack.pop();
                numDeleted += 1;
            }
            stack.push(num.charAt(i));
        }

        while(numDeleted < k) {
            stack.pop();
            numDeleted += 1;
        }

        StringBuilder ret = new StringBuilder();
        while (!stack.isEmpty())
            ret.append(stack.pop());

        if (ret.length() == 0)
            return "0";

        while (ret.length() > 1 && ret.charAt(ret.length() - 1) == '0')
            ret.deleteCharAt(ret.length() - 1);

        return ret.reverse().toString();
    }
}
