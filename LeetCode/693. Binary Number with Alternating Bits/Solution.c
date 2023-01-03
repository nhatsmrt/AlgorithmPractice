bool hasAlternatingBits(int n){
    // Time Complexity: O(log n)
    // Space Complexity: O(1)

    int parity = n % 2;
    n /= 2;

    while (n > 0) {
        if (n % 2 == parity)
            return false;

        parity = n % 2;
        n /= 2;
    }

    return true;
}
