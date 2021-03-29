class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # Time and Space Complexity: O(N)

        # Greedy: always try to extend the shortest chain if possible

        subseqs = {}

        for num in nums:
            if num not in subseqs:
                subseqs[num] = deque()

            if num - 1 in subseqs:
                shortest_len = subseqs[num - 1].popleft()

                if not subseqs[num - 1]:
                    subseqs.pop(num - 1)

                subseqs[num].append(shortest_len + 1)
            else:
                subseqs[num].appendleft(1)


        for num in subseqs:
            for len in subseqs[num]:
                if len < 3:
                    return False

        return True
