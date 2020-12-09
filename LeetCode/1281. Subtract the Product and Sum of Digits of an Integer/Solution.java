class Solution {
    public int subtractProductAndSum(int n) {
        List<Integer> digits = digits(n);

        return digits.stream().reduce(1, (x, y) -> x * y) - digits.stream().reduce(0, (x, y) -> x + y);
    }

    private List<Integer> digits(int n) {
        List<Integer> ret = new ArrayList<>();

        while (n > 0) {
            ret.add(n % 10);
            n /= 10;
        }

        return ret;
    }
}
