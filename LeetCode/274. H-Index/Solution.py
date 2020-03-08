class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Let cnt[i] = # of papers with i citations
        # cnt[N] = number of papers with at least N citations
        # We want to find max h (0 <= h <= N) such that:
        # sum(cnt[:h + 1]) >= N - h and sum(cnt[h:]) >= h

        cnt = [0 for i in range(len(citations) + 1)]
        for num in citations:
            cnt[min(num, len(citations))] += 1

        fewer_c = sum(cnt)
        more_c = 0
        # print(cnt)

        for h in range(len(citations), -1, -1):
            more_c += cnt[h]
            if fewer_c >= len(citations) - h and more_c >= h:
                    return h
            fewer_c -= cnt[h]

        return -1
            
