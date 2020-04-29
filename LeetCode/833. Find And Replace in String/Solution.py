class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        # Time Complexity: O(N + Q)

        queries = [
            [index, source, target]  for index, source, target in zip(indexes, sources, targets)
        ]

        # sort the queries
        buckets = [[] for i in range(len(S))]
        for q in queries:
            buckets[q[0]].append(q)

        queries = []
        for bucket in buckets:
            for q in bucket:
                queries.append(q)

        ret = []
        i = 0
        j = 0

        while i < len(S) and j < len(queries):
            if i < queries[j][0]:
                ret.append(S[i:queries[j][0]])
                i = queries[j][0]
            else:
                if S[i:i + len(queries[j][1])] == queries[j][1]:
                    ret.append(queries[j][2])
                else:
                    ret.append(S[i:i + len(queries[j][1])])

                i = i + len(queries[j][1])
                j += 1

        ret.append(S[i:])

        return ''.join(ret)
