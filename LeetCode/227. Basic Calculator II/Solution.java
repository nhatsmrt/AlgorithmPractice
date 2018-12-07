class Solution {
    // evaluate infix expression s
    public int calculate(String s) {

        List<String> postfixTokens = toPostfix(s);
        return evalRPN(postfixTokens);
    }

    // convert infix to postfix
    // using Dijkstra's Shunting yard algorithm
    private List<String> toPostfix(String s) {
        List<String> ret = new ArrayList<String>();
        Stack<String> operatorStack = new Stack<String>();

        int i = 0;
        while (i < s.length()) {
            char c = s.charAt(i);
            String op = "" + c;

            if (isNum(s.charAt(i))) {
                int j = i + 1;
                while (j < s.length() && isNum(s.charAt(j))) {
                    op += s.charAt(j);
                    j += 1;
                }

                i = j;
                ret.add(op);
                continue;
            }

            if(isOperator(op)) {
                while (!operatorStack.isEmpty() && !operatorStack.peek().equals("(") && compare(operatorStack.peek(), op) >= 0)
                    ret.add(operatorStack.pop());
                operatorStack.push(op);
            }
            else if (op.equals("("))
                operatorStack.push(op);
            else if (op.equals(")")) {
                while (!operatorStack.peek().equals("("))
                    ret.add(operatorStack.pop());
                operatorStack.pop();
            }

            i += 1;
        }

        while (!operatorStack.isEmpty())
            ret.add(operatorStack.pop());

        return ret;
    }

    private String eval(String leftOperand, String rightOperand, String operator) {
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

    private int evalRPN(List<String> tokens) {
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

    private boolean isOperator(String token) {
        return token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/");
    }

    private boolean isNum(char c) {
        return c >= '0' && c <= '9';
    }

    private int compare(String op1, String op2) {
        if ((op1.equals("+") || op1.equals("-")) && (op2.equals("*") || op2.equals("/")))
            return -1;
        else if ((op2.equals("+") || op2.equals("-")) && (op1.equals("*") || op1.equals("/")))
            return 1;
        else
            return 0;
    }

}
