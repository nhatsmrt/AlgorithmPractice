class Solution {
    public String intToRoman(int num) {
        String ret = "";

        while (num > 0) {
            if (num >= 1000) {
                int q = num / 1000;
                for (int i = 0; i < q; i++)
                    ret += "M";
                num -= q * 1000;
            }
            else if (num >= 900) {
                num -= 900;
                ret += "CM";
            }
            else if (num >= 500) {
                num -= 500;
                ret += "D";
            }
            else if (num >= 400) {
                num -= 400;
                ret += "CD";
            }
            else if (num >= 100) {
                int q = num / 100;
                for (int i = 0; i < q; i++)
                    ret += "C";
                num -= q * 100;
            }
            else if (num >= 90) {
                num -= 90;
                ret += "XC";
            }
            else if (num >= 50) {
                num -= 50;
                ret += "L";
            }
            else if (num >= 40) {
                num -= 40;
                ret += "XL";
            }
            else if (num >= 10) {
                int q = num / 10;
                for (int i = 0; i < q; i++)
                    ret += "X";
                num -= q * 10;
            }
            else if (num >= 9) {
                num -= 9;
                ret += "IX";
            }
            else if (num >= 5) {
                num -= 5;
                ret += "V";
            }
            else if (num >= 4) {
                num -= 4;
                ret += "IV";
            }
            else {
                for (int i = 0; i < num; i++)
                    ret += "I";
                num = 0 ;
            }
        }

        return ret;
    }
}
