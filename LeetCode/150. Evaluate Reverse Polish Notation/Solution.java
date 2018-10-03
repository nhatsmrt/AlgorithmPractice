class Solution {
    private boolean isOperator(String token) {
        return token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/");
    }

    public String eval(String leftOperand, String rightOperand, String operator) {
        Integer left = Integer.parseInt(leftOperand);
        Integer right = Integer.parseInt(rightOperand);
        String result = "";

        if (operator.equals("+"))
            result = Integer.toString(left + right);
        else if (operator.equals("-"))
            result = Integer.toString(left - right);
        else if (operator.equals("*"))
            result = Integer.toString(left * right);
        else
            result = Integer.toString(left / right);

        return result;

    }

    public int evalRPN(String[] tokens) {
        Stack<String> storage = new Stack<String>();

        for (String token : tokens) {
            if (isOperator(token)) {
                String rightOperand = storage.pop();
                String leftOperand = storage.pop();

                String result = eval(leftOperand, rightOperand, token);
                storage.push(result);
            }
            else {
                storage.push(token);
            }
        }

        return Integer.parseInt(storage.pop());
    }
}
