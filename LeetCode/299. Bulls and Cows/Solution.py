class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        same_digs = self.diff_cnter(self.get_counter(secret), self.get_counter(guess))
        same_place_dig = len(list(filter(lambda tup: tup[0] == tup[1], zip(secret, guess))))

        return str(same_place_dig) + "A" + str(same_digs - same_place_dig) + "B"

    def get_counter(self, num: str) -> Counter:
        cnter = Counter()
        for dig in num:
            cnter[dig] += 1

        return cnter

    def diff_cnter(self, cnt1: Counter, cnt2: Counter) -> str:
        digs = list(map(str, range(10)))
        same_digs = sum(map(lambda dig: min(cnt1[dig], cnt2[dig]), digs))
        return sum(map(lambda dig: min(cnt1[dig], cnt2[dig]), digs))
