class Solution:
    def confusingNumber(self, N: int) -> bool:
        confusing_digits = set([0, 1, 6, 8, 9])
        digit_map = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        changed = False
        new_num = 0
        old_num = N

        while N > 0:
            digit = N % 10
            if digit not in confusing_digits:
                return False
            changed = changed or (digit == 6) or (digit == 9)
            N = N // 10
            new_num = new_num * 10 + digit_map[digit]

        return new_num != old_num
