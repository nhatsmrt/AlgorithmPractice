class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        # Time and Space Complexity: O(log(N)^2)

        def get_digits(num: int) -> Counter:
            digs = []
            while num > 0:
                digs.append(num % 10)
                num //= 10

            return len(digs), Counter(digs)


        cur_pow = 1
        num_cur_pow_digs, cur_pow_digits = get_digits(cur_pow)
        num_digs, digits = get_digits(N)

        while num_cur_pow_digs <= num_digs and cur_pow_digits != digits:
            cur_pow *= 2
            num_cur_pow_digs, cur_pow_digits = get_digits(cur_pow)

        return cur_pow_digits == digits
