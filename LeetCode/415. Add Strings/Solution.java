class Solution {
    public String addStrings(String num1, String num2) {
        String ret = "";
        int rem = 0;
        int maxComDig = Math.min(num1.length(), num2.length());
        for (int i = 0; i < maxComDig; i++) {
            int firstDig = (int) (num1.charAt(num1.length() - 1 - i) - '0');
            int secondDig = (int) (num2.charAt(num2.length() - 1 - i) - '0');
            int sum = firstDig + secondDig + rem;
            rem = sum / 10;
            ret = sum % 10 + ret;
        }
        for (int i = maxComDig; i < num1.length(); i++) {
            int sum = (int)(num1.charAt(num1.length() - 1 - i) - '0') + rem;
            rem = sum / 10;
            ret = sum % 10 + ret;
        }
        for (int i = maxComDig; i < num2.length(); i++)  {
            int sum = (int) (num2.charAt(num2.length() - 1 - i) - '0') + rem;
            rem = sum / 10;
            ret = sum % 10 + ret;
        }
        if (rem != 0)
            ret = rem + ret;

        return ret;
    }
}
