class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        # Property 1: x, y, z forms an arithmetic progression (a.p) i.f.f
        # linearly transform them gives us another a.p:
        # 2(ay + b) = (ax + b) + (az + b)

        # Corolary: If A[0], ..., A[n - 1]
        # is a linearly transformed 1, ..., n
        # then a permutation of them is a.p-free
        # i.f.f the corresponding permutation of the indices
        # are also arithmetic free

        # Property 2: If x and z are odd, then no value of y
        # makes (x, y, z) an a.p

        # From these observations, we can derive the following DnC algorithm
        # to generate an a.p-free permutation of 1 to N:

        ## If an array has length <= 1, simply return it
        ## Otherwise, separate them into two halves: one with odd indices
        ## and the other with even indices
        ## ''Beautify'' each of them, then concatenate

        ## Invariant: Any subarray A that we call beautify on
        ## is linearly transformed from [1, ..., len(A)]

        # Time and space complexity: O(n log n)

        return self.beautify([num for num in range(1, N + 1)])

    def beautify(self, array: List[int]) -> List[int]:
        if len(array) <= 1:
            return array

        left = [array[i] for i in range(0, len(array), 2)]
        right = [array[i] for i in range(1, len(array), 2)]

        return self.beautify(left) + self.beautify(right)
