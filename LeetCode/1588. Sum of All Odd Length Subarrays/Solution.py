class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # Time and Space Complexity: O(N)

        # num_subarr[i] = # subarrays of odd length containing arr[i]
        # num_subarr[i] = (i + 2) // 2 * (len(arr) - i) // 2 + (i + 1) // 2 * (len(arr) - i + 1) // 2 - 1

        num_subarr = map(lambda i: ((i + 2) // 2) * ((len(arr) + 1 - i) // 2) + ((i + 1) // 2) * ((len(arr) - i) // 2), range(len(arr)))

        return reduce(lambda acc, pair: acc + pair[0] * pair[1], zip(num_subarr, arr), 0)
