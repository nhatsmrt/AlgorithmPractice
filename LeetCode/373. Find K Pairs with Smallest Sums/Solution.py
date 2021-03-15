class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Time Complexity: O(K log N)
        # Space Complexity: O(N)

        if not nums1 or not nums2:
            return []
        ret = []

        heap = [(nums1[i] + nums2[0], i, 0) for i in range(len(nums1))]
        heapq.heapify(heap)

        for _ in range(k):
            if heap:
                pair_sum, first_ind, second_ind = heapq.heappop(heap)
                ret.append([nums1[first_ind], nums2[second_ind]])

                if second_ind + 1 < len(nums2):
                    heapq.heappush(heap, (nums1[first_ind] + nums2[second_ind + 1], first_ind, second_ind + 1))
            else:
                break

        return ret
