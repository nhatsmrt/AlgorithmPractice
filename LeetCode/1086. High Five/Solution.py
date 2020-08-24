class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # Time and Space Complexity: O(N)

        ret = []
        scores = {}

        for item in items:
            if item[0] not in scores:
                scores[item[0]] = []

            scores[item[0]].append(item[1])

        for student_id in scores:
            heap = list(map(lambda score: -score, scores[student_id]))
            sorted_scores = []

            heapq.heapify(heap)
            n_elements = min(5, len(heap))

            for i in range(n_elements):
                sorted_scores.append(-heapq.heappop(heap))

            ret.append([student_id, sum(sorted_scores) // len(sorted_scores)])


        return ret
