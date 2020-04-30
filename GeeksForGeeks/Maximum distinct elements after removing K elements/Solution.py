#code
from typing import List
from collections import Counter
import heapq

# Time Complexity: O(K log N)
# Space Complexity: O(N)

def max_distinct_elements(arr: List[int], num_remove: int) -> int:
    cnter = Counter()

    for num in arr:
        cnter[num] += 1

    heap = []
    for num in cnter:
        heap.append((-cnter[num], num))
    heapq.heapify(heap)

    ret = len(cnter)
    for _ in range(num_remove):
        cnt, val = heapq.heappop(heap)
        cnt += 1

        if cnt == 0:
            ret -= 1
        else:
            heapq.heappush(heap, (cnt, val))

    return ret

num_tests = int(input())

for _ in range(num_tests):
    arr_len, num_remove = tuple(map(int, input().split(" ")))

    if arr_len > 0:
        arr = list(map(int, input().strip().split(" ")))
        print(max_distinct_elements(arr, num_remove))
    else:
        print(0)
