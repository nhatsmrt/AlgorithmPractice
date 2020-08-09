INSERT_CHAR = "<INSERT>"

def is_digit(character):
    return ord('0') <= ord(character) <= ord('9')

def is_lowercase(character):
    return ord('a') <= ord(character) <= ord('z')

def is_uppercase(character):
    return ord('A') <= ord(character) <= ord('Z')

def is_alphabetical(character):
    return is_lowercase(character) and is_uppercase(character)

class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        # Time and Space Complexity: O(N)

        self.dp = {}
        return self.minChange(s, 0, 0, "", False, False, False, False)

    def minChange(
        self, s: str, i: int, num_letter: int, last: str, same: bool,
        has_lowercase: bool, has_uppercase: bool, has_digit: bool
    ):
        key = (i, num_letter, last, same, has_lowercase, has_uppercase, has_digit)

        if key in self.dp:
            return self.dp[key]

        if num_letter > 20:
            ret = -1
        elif i == len(s):
            ret = 0

            if not has_lowercase:
                ret += 1

            if not has_uppercase:
                ret += 1

            if not has_digit:
                ret += 1

            num_letter += ret
            if num_letter > 20:
                ret = -1
            elif num_letter < 6:
                ret += 6 - num_letter
        elif num_letter == 20:
            if has_lowercase and has_uppercase and has_digit:
                ret = len(s) - i
            else:
                ret = -1
        else:
            candidates = []

            # Delete current character
            candidates.append(
                self.minChange(s, i + 1, num_letter, last, same, has_lowercase, has_uppercase, has_digit))

            # Add a character:
            candidates.append(
                self.minChange(s, i, num_letter + 1, INSERT_CHAR, False, True, has_uppercase, has_digit)) # insert a lowercase character
            candidates.append(
                self.minChange(s, i, num_letter + 1, INSERT_CHAR, False, has_lowercase, True, has_digit)) # insert an uppercase character
            candidates.append(
                self.minChange(s, i, num_letter + 1, INSERT_CHAR, False, has_lowercase, has_uppercase, True)) # insert a digit

            # Replace current character:
            candidates.append(
                self.minChange(s, i + 1, num_letter + 1, INSERT_CHAR, False, True, has_uppercase, has_digit)) # replace wwith a lowercase character
            candidates.append(
                self.minChange(s, i + 1, num_letter + 1, INSERT_CHAR, False, has_lowercase, True, has_digit)) # replace with an uppercase character
            candidates.append(
                self.minChange(s, i + 1, num_letter + 1, INSERT_CHAR, False, has_lowercase, has_uppercase, True)) # replace with a digit

            filtered_candidates = list(filter(lambda val: val != -1, candidates))
            ret = (1 + min(filtered_candidates)) if len(filtered_candidates) > 0 else -1

            # Keep current character:
            if not same or last != s[i]:
                new_same = s[i] == last
                new_last = s[i]

                new_lower = has_lowercase or is_lowercase(s[i])
                new_upper = has_uppercase or is_uppercase(s[i])
                new_dig = has_digit or is_digit(s[i])

                candidate = self.minChange(s, i + 1, num_letter + 1, new_last, new_same, new_lower, new_upper, new_dig)
                if candidate != -1:
                    ret = min(ret, candidate) if ret != -1 else candidate

        self.dp[key] = ret
        return ret
