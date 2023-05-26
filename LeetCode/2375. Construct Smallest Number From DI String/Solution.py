def construct(digits, used, pattern):
    if len(digits) == len(pattern) + 1:
        return "".join(digits)

    last_digits = int(digits[-1])

    if pattern[len(digits) - 1] == "I":
        for choice in range(last_digits + 1, 10):
            if choice not in used:
                digits.append(str(choice))
                used.add(choice)
                cand = construct(digits, used, pattern)

                if cand:
                    return cand

                digits.pop()
                used.remove(choice)
    else:
        for choice in range(1, last_digits):
            if choice not in used:
                digits.append(str(choice))
                used.add(choice)
                cand = construct(digits, used, pattern)

                if cand:
                    return cand

                digits.pop()
                used.remove(choice)
    return None

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        for first_digit in range(1, 10):
            cand = construct([str(first_digit)], set([first_digit]), pattern)

            if cand:
                return cand

        return None
