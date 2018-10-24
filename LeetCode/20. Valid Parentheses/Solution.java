class Solution {
    public boolean isValid(String s) {
        int strLen = s.length();
        if (strLen % 2 != 0)
            return false;

        Stack<Character> storage = new Stack<Character>();
        for (int i = 0; i < strLen; i++) {
            char bracket = s.charAt(i);
            if (isOpen(bracket))
                storage.push(bracket);
            else {
                if (storage.isEmpty())
                    return false;
                else {
                    char open = storage.pop();
                    if (!isValid(open, bracket))
                        return false;
                }
            }
        }

        return storage.isEmpty();
    }

    private boolean isValid(char open, char close) {
        return (open == '[' && close == ']') || (open == '(' && close == ')') || (open == '{' && close == '}');
    }

    private boolean isOpen (char bracket) {
        return bracket == '[' || bracket == '(' || bracket == '{';
    }
}
