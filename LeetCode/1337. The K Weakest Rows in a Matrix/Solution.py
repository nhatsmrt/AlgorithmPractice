class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Time Complexity: O(M log N + M log K)
        # Space Complexity: O(M)

        def cnt_soldiers(row: List[int]) -> int:
            low = 0
            high = len(row)

            while low < high:
                mid = high - (high - low) // 2

                if row[mid - 1]:
                    low = mid
                else:
                    high = mid - 1


            return low

        soldier_cnts = list(zip(map(cnt_soldiers, mat), range(len(mat))))
        heapq.heapify(soldier_cnts)
        ret = []

        for _ in range(k):
            ret.append(heapq.heappop(soldier_cnts)[1])

        return ret
