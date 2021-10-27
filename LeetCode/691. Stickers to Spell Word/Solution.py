def string_to_char_cnt(string):
    ret = [0] * 26

    for char in string:
        ret[ord(char) - ord('a')] += 1

    return tuple(ret)

def use(string, sticker):
    return tuple(map(lambda pair: max(0, pair[0] - pair[1]), zip(string, sticker)))


INF = 1000000000


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # Time Complexity: O(
        #                    |target| + sum(|sticker| in stickers) +
        #                    |stickers| prod_{'a' <= c = 'z'} (cnt(target, c) + 1))
        # Space Complexity: O(|stickers| prod_{'a' <= c = 'z'} (cnt(target, c) + 1))

        stickers = list(map(string_to_char_cnt, stickers))
        target = string_to_char_cnt(target)

        self.dp = {}

        ret = self.build(stickers, 0, target)

        if ret >= INF:
            return -1

        return ret


    def build(self, stickers, i, remaining):
        if (i, remaining) in self.dp:
            return self.dp[(i, remaining)]

        remaining_cnt = sum(remaining)

        if not remaining_cnt:
            return 0

        if i == len(stickers):
            return INF

        ret = self.build(stickers, i + 1, remaining) # not use stickers[i]

        used = use(remaining, stickers[i])
        if used != remaining:
            ret = min(ret, 1 + self.build(stickers, i, used))

        self.dp[(i, remaining)] = ret
        return ret
