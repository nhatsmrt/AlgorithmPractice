class Solution {
    public int[] numbersWithUniqueDigits;
    public int[] numbersWithNUniqueDigits;

    public int countNumbersWithUniqueDigitsDP(int n) {
        if (n > 10)
            return countNumbersWithUniqueDigitsDP(10);

        if (numbersWithUniqueDigits[n] != -1)
            return numbersWithUniqueDigits[n];

        numbersWithUniqueDigits[n] = countNumbersWithUniqueDigitsDP(n - 1) +
            countNumbersWithNUniqueDigitsDP(n);

        return numbersWithUniqueDigits[n];
    }

    public int countNumbersWithNUniqueDigitsDP(int n) {
        if (n > 10)
            return 0;

        if (numbersWithNUniqueDigits[n] != -1)
            return numbersWithNUniqueDigits[n];

        numbersWithNUniqueDigits[n] = countNumbersWithNUniqueDigitsDP(n - 1) * (11 - n);

        return numbersWithNUniqueDigits[n];
    }
    public int countNumbersWithUniqueDigits(int n) {
        numbersWithUniqueDigits = new int[11];
        numbersWithNUniqueDigits = new int[11];

        if (n == 0)
            return 1;

        Arrays.fill(numbersWithUniqueDigits, -1);
        Arrays.fill(numbersWithNUniqueDigits, -1);
        numbersWithUniqueDigits[1] = 10;
        numbersWithNUniqueDigits[1] = 9;
        numbersWithNUniqueDigits[2] = 81;

        return countNumbersWithUniqueDigitsDP(n);
    }
}
