class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # Time Complexity: O(N^3)
        # Space Complexity: O(1)

        for end1 in range(len(num) - 1):
            for end2 in range(end1 + 1, len(num)):
                if (num[0] == '0' and end1 != 0) or (num[end1 + 1] == '0' and end2 != end1 + 1):
                    continue

                first = int(num[:end1 + 1])
                second = int(num[end1 + 1:end2 + 1])
                found_third = False

                cur = end2 + 1

                while cur < len(num):
                    next = first + second
                    next_str = str(next)

                    if len(next_str) > len(num) - cur or next_str != num[cur:cur + len(next_str)]:
                        break

                    first, second = second, next
                    found_third = True
                    cur += len(next_str)
                else:
                    if found_third:
                        return True

        return False
