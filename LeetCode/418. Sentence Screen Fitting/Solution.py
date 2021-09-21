class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        # Time Complexity: O(SN + M)
        # Space Complexity: O(S)

        can_fit = []

        for start_ind in range(len(sentence)):
            sent_ind = start_ind
            i = 0
            full_sent = 0

            while i < cols:
                word = sentence[sent_ind]
                if i + len(word) - 1 < cols:
                    i += len(word) + 1
                    sent_ind += 1

                    if sent_ind == len(sentence):
                        sent_ind = 0
                        full_sent += 1
                else:
                    break

            can_fit.append((sent_ind, full_sent))

        sent_ind = 0
        ret = 0
        for _ in range(rows):
            sent_ind, full_sent = can_fit[sent_ind]
            ret += full_sent

        return ret
