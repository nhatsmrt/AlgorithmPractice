class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # Time and Space Complexity: O(N)

        counter = Counter(arr)
        sizes = [counter[val] for val in counter]
        buckets = [0] * len(arr)

        for size in sizes:
            buckets[size - 1] += 1

        cur = 0
        for (val, bucket_size) in enumerate(buckets):
            for i in range(bucket_size):
                sizes[cur] = val + 1
                cur += 1

        sizes = list(reversed(sizes))
        cur_rem = 0
        i = 0
        target = (len(arr) + 1) // 2

        while cur_rem < target:
            cur_rem += sizes[i]
            i += 1

        return i
        
