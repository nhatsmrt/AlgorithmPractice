# Time Complexity: <O(n), O(log n) w.h.p>
# Space Complexity: O(n)
from random import randint


class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.inverted_ind = {}
        for i in range(len(arr)):
            num = arr[i]

            if num not in self.inverted_ind:
                self.inverted_ind[num] = []

            self.inverted_ind[num].append(i)

        self.num_iter = 7


    def query(self, left: int, right: int, threshold: int) -> int:
        for i in range(self.num_iter):
            maj = self.arr[randint(left, right)]

            first = bisect.bisect_left(self.inverted_ind[maj], left)
            last = bisect.bisect_right(self.inverted_ind[maj], right)

            if last - first >= threshold:
                return maj
        return -1





# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
