class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        # Time Complexity: O(N^4)
        # Space Complexity: O(N^3)

        condensed_boxes = []
        start = 0

        for i, col in enumerate(boxes):
            if col != boxes[start]:
                condensed_boxes.append((boxes[start], i - start))
                start = i
        condensed_boxes.append((boxes[start], len(boxes) - start))
        boxes = condensed_boxes

        index = {}
        next_index = {}

        for i, (col, _) in enumerate(boxes):
            if col not in index:
                index[col] = [i]
            else:
                next_index[index[col][-1]] = i
                index[col].append(i)

        self.next_index = next_index
        self.dp = {}
        return self.getScore(condensed_boxes, 0, len(condensed_boxes) - 1, condensed_boxes[0][1])


    def getScore(self, boxes, start: int, end: int, startRep: int) -> int:
        if (start, end, startRep) in self.dp:
            return self.dp[(start, end, startRep)]

        if start > end:
            return 0
        if start == end:
            ret = startRep ** 2
        else:
            ret = startRep ** 2 + self.getScore(boxes, start + 1, end, boxes[start + 1][1])

            next_occ = self.next_index.get(start, -1)

            while next_occ >= 0 and next_occ <= end:
                ret = max(ret, self.getScore(boxes, start + 1, next_occ - 1, boxes[start + 1][1]) + self.getScore(boxes, next_occ, end, startRep + boxes[next_occ][1]))
                next_occ = self.next_index.get(next_occ, -1)

        self.dp[(start, end, startRep)] = ret
        return ret
