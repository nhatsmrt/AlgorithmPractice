class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Time and Space Complexity: O(N)
        record = []

        for token in operations:
            if token not in "+DC":
                record.append(int(token))
            elif token == "C":
                record.pop()
            elif token == "D":
                record.append(record[-1] * 2)
            elif token == "+":
                record.append(record[-1] + record[-2])

        return sum(record)
