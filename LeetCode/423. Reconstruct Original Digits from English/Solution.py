class Solution:
    def originalDigits(self, s: str) -> str:
        # Time and Space Complexity: O(|s|)
        cnter = Counter(s)
        digit_words = [
            "zero", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine"
        ]
        digit_counters = list(map(Counter, digit_words))

        has_char = {}
        for i, counter in enumerate(digit_counters):
            for char in counter:
                if char not in has_char:
                    has_char[char] = set()

                has_char[char].add(i)

        ready = [(next(iter(has_char[char])), char) for char in has_char if len(has_char[char]) == 1]
        ready_set = set(next(iter(has_char[char])) for char in has_char if len(has_char[char]) == 1)
        ret_cnt = {}

        while ready:
            digit, unique_char = ready.pop()
            multiples = cnter[unique_char] // digit_counters[digit][unique_char]
            ret_cnt[digit] = multiples

            for char in digit_counters[digit]:
                cnter[char] -= multiples * digit_counters[digit][char]

                # update has_char:
                if digit in has_char[char]:
                    has_char[char].remove(digit)

                if len(has_char[char]) == 1 and next(iter(has_char[char])) not in ready_set:
                    ready_set.add(next(iter(has_char[char])))
                    ready.append((next(iter(has_char[char])), char))

        ret = []
        for i in range(10):
            ret.extend([str(i)] * ret_cnt[i])

        return "".join(ret)
