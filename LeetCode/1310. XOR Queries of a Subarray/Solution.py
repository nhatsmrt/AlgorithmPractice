class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0]
        for num in arr:
            prefix_xor.append(num ^ prefix_xor[-1])


        ret = []
        for query in queries:
            ret.append(prefix_xor[query[1] + 1] ^ prefix_xor[query[0]])

        return ret
