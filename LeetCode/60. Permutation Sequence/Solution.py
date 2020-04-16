class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Idea: construct the sequence from left to right
        # At position i (1 <= i <= n), we use the jth remaining number if
        # j (n - i)! < remaining k <= (j + 1) (n - i)!

        # Time complexity: O(n^2)
        # (can be reduced to O(n log n)) if use an order statistics tree
        # to store the remaining numbers)
        # Space complexity: O(n)


        factorials = [1, 1]
        for i in range(2, n):
            factorials.append(factorials[-1] * i)
        print(factorials)


        numbers = [i for i in range(1, n + 1)]


        ret = []
        for i in range(1, n + 1):
            if k % factorials[n - i] == 0:
                ind = k // factorials[n - i] - 1
            else:
                ind = k // factorials[n - i]

            k -= ind * factorials[n - i]
            ret.append(numbers.pop(ind))

        return ''.join([str(val) for val in ret])
