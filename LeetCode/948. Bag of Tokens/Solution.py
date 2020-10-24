class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()

        start = 0
        end = len(tokens) - 1

        score = 0
        ret = 0

        while start <= end:
            if tokens[start] <= P:
                score += 1
                P -= tokens[start]
                start += 1
            else:
                if score > 0:
                    score -= 1
                    P += tokens[end]
                    end -= 1
                else:
                    break

            ret = max(score, ret)

        return ret
