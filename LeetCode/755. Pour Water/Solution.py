class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        # Time Complexity: O((V + N) log N)
        # Space Complexity: O(N)

        left_pq = []
        right_pq = []
        added_ind = set()

        for i in range(K - 1, -1, -1):
            if heights[i] > heights[i + 1]:
                break

            left_pq.append((heights[i], -i)) # prefer closer index
            added_ind.add(i)

        for i in range(K + 1, len(heights)):
            if heights[i] > heights[i - 1]:
                break

            right_pq.append((heights[i], i)) # prefer closer index
            added_ind.add(i)

        heapq.heapify(left_pq)
        heapq.heapify(right_pq)

        for _ in range(V):
            if left_pq and left_pq[0][0] < heights[K]: # water can flow left
                height, neg_ind = heapq.heappop(left_pq)
                ind = -neg_ind
                heights[ind] += 1
                heapq.heappush(left_pq, (heights[ind], -ind))


                add_ind = ind - 1
                while add_ind not in added_ind and add_ind >= 0 and heights[add_ind] <= heights[add_ind + 1]:
                    heapq.heappush(left_pq, (heights[add_ind], -add_ind))
                    added_ind.add(add_ind)
                    add_ind -= 1

            elif right_pq and right_pq[0][0] < heights[K]: # water can flow right
                height, ind = heapq.heappop(right_pq)
                heights[ind] += 1
                heapq.heappush(right_pq, (heights[ind], ind))

                add_ind = ind + 1
                while add_ind not in added_ind and add_ind < len(heights) and heights[add_ind] <= heights[add_ind - 1]:
                    heapq.heappush(right_pq, (heights[add_ind], add_ind))
                    added_ind.add(add_ind)
                    add_ind += 1

            else:
                heights[K] += 1

                add_ind = K - 1
                while add_ind not in added_ind and add_ind >= 0 and heights[add_ind] <= heights[add_ind + 1]:
                    heapq.heappush(left_pq, (heights[add_ind], -add_ind))
                    added_ind.add(add_ind)
                    add_ind -= 1


                add_ind = K + 1
                while add_ind not in added_ind and add_ind < len(heights) and heights[add_ind] <= heights[add_ind - 1]:
                    heapq.heappush(right_pq, (heights[add_ind], add_ind))
                    added_ind.add(add_ind)
                    add_ind += 1

        return heights
