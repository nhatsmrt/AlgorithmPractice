class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        indeg = [0] * N
        outdeg = [0] * N

        for t in trust:
            indeg[t[1] - 1] += 1
            outdeg[t[0] - 1] += 1

        satisfy = []

        for i in range(N):
            if indeg[i] == N - 1 and outdeg[i] == 0:
                satisfy.append(i)

        return (satisfy[0] + 1) if len(satisfy) == 1 else -1
        
