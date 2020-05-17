from collections import Counter


class Solution:
    def countElements(self, arr: List[int]) -> int:
        cnter = Counter()
        for num in arr:
            cnter[num] += 1

        ret = 0
        for num in cnter:
            if num + 1 in cnter:
                ret += cnter[num]

        return ret
