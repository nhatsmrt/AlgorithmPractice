class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        cnter = Counter(A)
        only_once = [val for val in cnter if cnter[val] == 1]
        return max(only_once) if only_once else -1
