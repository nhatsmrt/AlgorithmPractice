class Polynomial {
    private int[] coeffs;

    public Polynomial(String num) {
        coeffs = new int[num.length()];
        for (int i = 0; i < num.length(); i++) {
            coeffs[i] = (int) (num.charAt(num.length() - 1 - i) - '0');
        }
    }

    public Polynomial(int order) {
        coeffs = new int[order + 1];
    }

    public Polynomial multiply(Polynomial other) {
        Polynomial res = new Polynomial(order() + other.order());
        for (int i = 0; i < res.order() + 1; i++) {
            for (int j = 0; j <= i; j++) {
                if (j <= order() && i - j <= other.order())
                    res.coeffs[i] += coeffs[j] * other.coeffs[i - j];
            }
        }

        return res;
    }

    public String toString() {
        StringBuilder reverse = new StringBuilder();
        int remainder = 0;
        int cur = 0;

        for (int i = 0; i < coeffs.length; i++) {
            cur = coeffs[i] + remainder;
            reverse.append(cur % 10);
            remainder = cur / 10;
        }

        if (remainder != 0)
            reverse.append(remainder);

        while(reverse.charAt(reverse.length() - 1) == '0' && reverse.length() > 1)
            reverse.deleteCharAt(reverse.length() - 1);

        return reverse.reverse().toString();
    }

    public int order() {
        return coeffs.length - 1;
    }
}


class Solution {
    public String multiply(String num1, String num2) {
        if (num1 == "0" || num2 == "0")
            return "0";

        Polynomial poly1 = new Polynomial(num1);
        Polynomial poly2 = new Polynomial(num2);

        return poly1.multiply(poly2).toString();
    }
}
